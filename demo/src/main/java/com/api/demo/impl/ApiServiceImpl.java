package com.api.demo.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.api.demo.constants.ConstantMessage;
import com.api.demo.dto.ApiResponseDTO;
import com.api.demo.service.ApiService;
import com.api.demo.util.CommonUtil;

@Service
public class ApiServiceImpl implements ApiService {


  private RestTemplate restTemplate;

	private final String url = "https://api.bittrex.com/api/v1.1/public/getticker?market=";
    
	ApiServiceImpl(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;     
	}
	
	  
	public ApiResponseDTO getCurrencyDetail(String queryParam) {
	  ApiResponseDTO response;
	
	    if (CommonUtil.isValidQuery(queryParam)) {	
		  response = restTemplate.getForObject(url+queryParam, ApiResponseDTO.class);
		  return response;
	    }
		else {
		 response = new ApiResponseDTO();
		 response.setMessage(ConstantMessage.INVALID_QUERY);
	 	return response;
	   }

	}
}
