package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.web.client.RestTemplate;

import com.api.demo.constants.ConstantMessage;
import com.api.demo.dto.ApiResponseDTO;
import com.api.demo.impl.ApiServiceImpl;

@ActiveProfiles("test")
@RunWith(SpringRunner.class)
@SpringBootTest(classes =  {RestTemplate.class, ApiServiceImpl.class})
public class DemoApplicationTests {

	@Autowired
	private ApiServiceImpl apiServiceImpl;
	
	@Test 
	public void testCallAPIService() {
		ApiResponseDTO response = apiServiceImpl.getCurrencyDetail("BTC-*LTC");
		assertEquals(false, response.isSuccess());
		assertEquals(ConstantMessage.INVALID_QUERY, response.getMessage());
	 }
	@Test 
	public void testCallAPIServiceValid() {
		ApiResponseDTO response = apiServiceImpl.getCurrencyDetail("BTC-LTC");
		 assertEquals(true, response.isSuccess());
		 assertEquals("", response.getMessage());
	 }
			 
	
	
	
	
	 

}
