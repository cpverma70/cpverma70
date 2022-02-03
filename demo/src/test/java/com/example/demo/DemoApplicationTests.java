package com.example.demo;


import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;

import org.junit.Before;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mockito;
import org.mockito.junit.MockitoJUnitRunner;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Profile;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.client.RestTemplate;

import com.api.demo.constants.ConstantMessage;
import com.api.demo.controller.RestController;
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
