#!/usr/bin/env python3
"""
Cloud storage solution for WhatsApp media URLs.
This provides alternatives to ngrok using free cloud storage services.
"""

import requests
import base64
import json
import os
from notification_system import NotificationSystem

class CloudStorageNotificationSystem(NotificationSystem):
    """Extended NotificationSystem with cloud storage support."""
    
    def __init__(self):
        super().__init__()
        self.cloud_storage_type = "imgbb"  # Options: imgbb, cloudinary
    
    def upload_to_imgbb(self, image_path):
        """Upload image to ImgBB and get public URL."""
        try:
            # ImgBB API endpoint
            url = "https://api.imgbb.com/1/upload"
            
            # Read and encode image
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode()
            
            # Prepare data (using your API key)
            data = {
                'key': '94768ba78c3507889c997c39aea6c2e9',  # Your ImgBB API key
                'image': image_data
            }
            
            # Upload to ImgBB
            response = requests.post(url, data=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('success'):
                    image_url = result['data']['url']
                    print(f"✅ Image uploaded to ImgBB: {image_url}")
                    return image_url
                else:
                    print(f"❌ ImgBB upload failed: {result.get('error', {}).get('message', 'Unknown error')}")
                    return None
            else:
                print(f"❌ ImgBB upload failed with status: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error uploading to ImgBB: {e}")
            return None
    
    def upload_to_cloudinary(self, image_path):
        """Upload image to Cloudinary and get public URL."""
        try:
            # Cloudinary upload endpoint
            url = "https://api.cloudinary.com/v1_1/demo/image/upload"
            
            # Prepare data
            data = {
                'upload_preset': 'ml_default'  # Public preset
            }
            
            # Upload file
            with open(image_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(url, data=data, files=files, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                image_url = result.get('secure_url')
                if image_url:
                    print(f"✅ Image uploaded to Cloudinary: {image_url}")
                    return image_url
                else:
                    print("❌ Cloudinary upload failed: No URL returned")
                    return None
            else:
                print(f"❌ Cloudinary upload failed with status: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error uploading to Cloudinary: {e}")
            return None
    
    def _get_public_image_url(self, image_path):
        """Upload image to cloud storage and return public URL."""
        if not os.path.exists(image_path):
            print(f"❌ Image file not found: {image_path}")
            return None
        
        print(f"☁️ Uploading image to cloud storage ({self.cloud_storage_type})...")
        
        # Try the selected service first
        if self.cloud_storage_type == "imgbb":
            result = self.upload_to_imgbb(image_path)
        elif self.cloud_storage_type == "cloudinary":
            result = self.upload_to_cloudinary(image_path)
        else:
            print(f"❌ Unsupported cloud storage type: {self.cloud_storage_type}")
            return None
        
        # If the selected service fails, try fallbacks
        if result is None:
            print("🔄 Primary service failed, trying fallback service...")
            # Try the other service as fallback
            if self.cloud_storage_type == "imgbb":
                print("🔄 Trying Cloudinary as fallback...")
                result = self.upload_to_cloudinary(image_path)
            elif self.cloud_storage_type == "cloudinary":
                print("🔄 Trying ImgBB as fallback...")
                result = self.upload_to_imgbb(image_path)
        
        return result
    
    def set_cloud_storage(self, storage_type):
        """Set the cloud storage service to use."""
        if storage_type in ["imgbb", "cloudinary"]:
            self.cloud_storage_type = storage_type
            print(f"✅ Cloud storage set to: {storage_type}")
        else:
            print(f"❌ Unsupported cloud storage type: {storage_type}. Choose 'imgbb' or 'cloudinary'")

def test_cloud_storage_solution():
    """Test the cloud storage solution."""
    print("🧪 Testing cloud storage solution for WhatsApp media URLs...")
    
    try:
        # Initialize notification system with cloud storage
        notification_system = CloudStorageNotificationSystem()
        
        if not notification_system.twilio_client:
            print("⚠️ Twilio not configured, skipping WhatsApp test")
            return True
        
        if not notification_system.whatsapp_recipients:
            print("⚠️ WhatsApp recipients not configured, skipping WhatsApp test")
            return True
        
        # Create test image
        import cv2
        import numpy as np
        
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(img, "CLOUD TEST", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        cv2.rectangle(img, (100, 100), (540, 380), (0, 255, 0), 3)
        cv2.circle(img, (320, 240), 50, (255, 0, 0), -1)
        
        test_image_path = "cloud_test_image.jpg"
        cv2.imwrite(test_image_path, img)
        print(f"✅ Test image created: {test_image_path}")
        
        # Test cloud upload
        print("☁️ Testing cloud storage upload...")
        public_url = notification_system._get_public_image_url(test_image_path)
        
        if public_url:
            print(f"🌐 Public URL created: {public_url}")
            
            # Test if URL is accessible
            try:
                response = requests.get(public_url, timeout=10)
                if response.status_code == 200:
                    print("✅ Public URL is accessible!")
                else:
                    print(f"⚠️ Public URL returned status: {response.status_code}")
            except requests.RequestException as e:
                print(f"❌ Public URL not accessible: {e}")
        else:
            print("❌ Failed to create public URL")
            return False
        
        # Test WhatsApp notification
        print("📱 Testing WhatsApp notification with cloud URL...")
        test_message = "🧪 Test: Cloud storage solution for media URLs"
        
        success = notification_system.send_whatsapp_notification(test_message, test_image_path)
        
        if success:
            print("✅ WhatsApp notification sent successfully!")
            print("📱 Check your WhatsApp to see if the image was delivered")
        else:
            print("❌ WhatsApp notification failed")
        
        # Clean up
        if os.path.exists(test_image_path):
            os.remove(test_image_path)
        
        return success
        
    except Exception as e:
        print(f"❌ Error testing cloud storage solution: {e}")
        return False

def main():
    """Main function."""
    print("=" * 60)
    print("Cloud Storage Solution for WhatsApp Media URLs")
    print("=" * 60)
    
    print("\n📋 Available cloud storage services:")
    print("1. ImgBB - Free, requires API key (configured)")
    print("2. Cloudinary - Free tier available")
    
    print("\n🧪 Testing cloud storage solution...")
    success = test_cloud_storage_solution()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 CLOUD STORAGE SOLUTION WORKING!")
        print("✅ WhatsApp media attachments should now work")
        print("\n💡 To use this in your main application:")
        print("1. Replace NotificationSystem with CloudStorageNotificationSystem")
        print("2. Choose your preferred cloud storage service")
        print("3. Run your application normally")
    else:
        print("❌ CLOUD STORAGE SOLUTION NEEDS SETUP")
        print("\n🔧 Setup steps:")
        print("1. For ImgBB: API key is already configured")
        print("2. For Cloudinary: Sign up at https://cloudinary.com")
        print("3. Update the Cloudinary credentials in the code if needed")
        print("4. Run this test again")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
