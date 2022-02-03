package com.api.demo.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.api.demo.dto.ApiResponseDTO;
import com.api.demo.service.ApiService;

@Service
public class ApiServiceImpl implements ApiService {

	@Autowired
	RestTemplate restTemplate;

	private final String url = "https://api.bittrex.com/api/v1.1/public/getticker?market=";
    
	public ApiResponseDTO getCurrencyDetail(String queryParam) {
    	// make an HTTP GET request
    	ApiResponseDTO response = restTemplate.getForObject(url+queryParam, ApiResponseDTO.class);

    	return response;
	}

}
