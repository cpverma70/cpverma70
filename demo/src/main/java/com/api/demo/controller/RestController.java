package com.api.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.api.demo.constants.ConstantMessage;
import com.api.demo.dto.ApiResponseDTO;
import com.api.demo.service.ApiService;
import com.api.demo.util.CommonUtil;

@Controller
@RequestMapping("/api")
public class RestController {
	
   @Autowired
   ApiService apiService;
	
   @GetMapping("/test")
   public ResponseEntity<ApiResponseDTO> callApi(@RequestParam(name="currency") String queryParam) {
		 ApiResponseDTO response =null;
		 
	    if (CommonUtil.isValidQuery(queryParam)) {	
		    response = apiService.getCurrencyDetail(queryParam);	
		  return ResponseEntity.ok().body(response);
	    }
		else {
		 response = new ApiResponseDTO();
		  response.setMessage(ConstantMessage.INVALID_QUERY);
	     return ResponseEntity.badRequest().body(response);
	   }
	}

}
