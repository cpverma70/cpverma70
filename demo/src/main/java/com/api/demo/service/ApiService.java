package com.api.demo.service;

import com.api.demo.dto.ApiResponseDTO;

public interface ApiService {
	
	public ApiResponseDTO getCurrencyDetail(String queryParam);

}
