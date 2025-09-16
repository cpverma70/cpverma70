import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from twilio.rest import Client
import cv2
import os
import threading
from datetime import datetime
from config import Config

class NotificationSystem:
    def __init__(self):
        """Initialize notification system."""
        self.email_sender = Config.EMAIL_SENDER
        self.email_password = Config.EMAIL_PASSWORD
        self.email_recipients = Config.EMAIL_RECIPIENTS
        
        self.twilio_account_sid = Config.TWILIO_ACCOUNT_SID
        self.twilio_auth_token = Config.TWILIO_AUTH_TOKEN
        self.twilio_whatsapp_from = Config.TWILIO_WHATSAPP_FROM
        self.whatsapp_recipients = Config.WHATSAPP_RECIPIENTS
        
        # Initialize Twilio client
        if self.twilio_account_sid and self.twilio_auth_token:
            self.twilio_client = Client(self.twilio_account_sid, self.twilio_auth_token)
        else:
            self.twilio_client = None
            print("⚠️ Twilio credentials not configured. WhatsApp notifications disabled.")
    
    def send_whatsapp_notification(self, message, image_path=None):
        """
        Send WhatsApp notification via Twilio.
        
        Args:
            message: Message to send
            image_path: Optional path to image to send
        """
        if not self.twilio_client:
            print("❌ WhatsApp notification failed: Twilio not configured")
            return False
        
        def _send_whatsapp():
            try:
                for recipient in self.whatsapp_recipients:
                    if not recipient.strip():
                        continue
                        
                    print(f"📱 Sending WhatsApp to {recipient}...")
                    
                    if image_path and os.path.exists(image_path):
                        # Send message with image
                        message_obj = self.twilio_client.messages.create(
                            body=message,
                            from_=self.twilio_whatsapp_from,
                            to=recipient.strip(),
                            media_url=[f"file://{os.path.abspath(image_path)}"]
                        )
                    else:
                        # Send text message only
                        message_obj = self.twilio_client.messages.create(
                            body=message,
                            from_=self.twilio_whatsapp_from,
                            to=recipient.strip()
                        )
                    
                    print(f"✅ WhatsApp sent successfully to {recipient} (SID: {message_obj.sid})")
                    
            except Exception as e:
                print(f"❌ WhatsApp notification failed: {e}")
                return False
            
            return True
        
        # Send in separate thread to avoid blocking
        whatsapp_thread = threading.Thread(target=_send_whatsapp)
        whatsapp_thread.daemon = True
        whatsapp_thread.start()
        
        return True
    
    def send_email_notification(self, subject, message, image_path=None):
        """
        Send email notification.
        
        Args:
            subject: Email subject
            message: Email message
            image_path: Optional path to image to attach
        """
        if not self.email_sender or not self.email_password:
            print("❌ Email notification failed: Email credentials not configured")
            return False
        
        def _send_email():
            try:
                # Create message
                msg = MIMEMultipart()
                msg['From'] = self.email_sender
                msg['Subject'] = subject
                
                # Add body to email
                msg.attach(MIMEText(message, 'plain'))
                
                # Add image attachment if provided
                if image_path and os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        img_data = f.read()
                        image = MIMEImage(img_data)
                        image.add_header('Content-Disposition', 
                                       f'attachment; filename=detection_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg')
                        msg.attach(image)
                
                # Create SMTP session
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()  # Enable security
                server.login(self.email_sender, self.email_password)
                
                # Send emails to all recipients
                for recipient in self.email_recipients:
                    if not recipient.strip():
                        continue
                        
                    print(f"📧 Sending email to {recipient}...")
                    msg['To'] = recipient.strip()
                    
                    text = msg.as_string()
                    server.sendmail(self.email_sender, recipient.strip(), text)
                    print(f"✅ Email sent successfully to {recipient}")
                    
                    # Remove the 'To' header for next recipient
                    del msg['To']
                
                server.quit()
                
            except Exception as e:
                print(f"❌ Email notification failed: {e}")
                return False
            
            return True
        
        # Send in separate thread to avoid blocking
        email_thread = threading.Thread(target=_send_email)
        email_thread.daemon = True
        email_thread.start()
        
        return True
    
    def send_detection_alert(self, detection_count, confidence_scores, frame=None):
        """
        Send complete detection alert via all configured channels.
        
        Args:
            detection_count: Number of humans detected
            confidence_scores: List of confidence scores
            frame: Optional OpenCV frame to save and send
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Prepare message
        if detection_count == 1:
            message = f"🚨 SECURITY ALERT 🚨\n\n"
            message += f"Human detected at {timestamp}\n"
            message += f"Confidence: {max(confidence_scores):.2f}\n"
            message += f"Location: Security Camera\n\n"
            message += "Please check the premises immediately."
        else:
            message = f"🚨 SECURITY ALERT 🚨\n\n"
            message += f"{detection_count} humans detected at {timestamp}\n"
            message += f"Confidence scores: {[f'{score:.2f}' for score in confidence_scores]}\n"
            message += f"Location: Security Camera\n\n"
            message += "Multiple people detected. Please check the premises immediately."
        
        # Save frame as image if provided
        image_path = None
        if frame is not None:
            image_path = f"detection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Detection image saved: {image_path}")
        
        # Send notifications
        print("📢 Sending notifications...")
        
        # WhatsApp notification
        if self.whatsapp_recipients:
            self.send_whatsapp_notification(message, image_path)
        
        # Email notification
        if self.email_recipients:
            subject = f"🚨 Security Alert - Human Detection - {timestamp}"
            self.send_email_notification(subject, message, image_path)
        
        # Clean up temporary image file after a delay
        if image_path:
            def cleanup():
                import time
                time.sleep(60)  # Wait 1 minute before cleanup
                try:
                    if os.path.exists(image_path):
                        os.remove(image_path)
                        print(f"Cleaned up temporary file: {image_path}")
                except Exception as e:
                    print(f"Error cleaning up {image_path}: {e}")
            
            cleanup_thread = threading.Thread(target=cleanup)
            cleanup_thread.daemon = True
            cleanup_thread.start()
    
    def test_notifications(self):
        """Test all notification systems."""
        print("🧪 Testing notification systems...")
        
        test_message = f"Test notification from Human Detection System at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Test WhatsApp
        if self.whatsapp_recipients:
            print("Testing WhatsApp...")
            self.send_whatsapp_notification("🧪 " + test_message)
        
        # Test Email
        if self.email_recipients:
            print("Testing Email...")
            self.send_email_notification("🧪 Test - Human Detection System", test_message)
        
        print("Test notifications sent!")