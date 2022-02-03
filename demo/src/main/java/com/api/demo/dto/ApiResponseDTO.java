package com.api.demo.dto;


public class ApiResponseDTO {
	
	private boolean success;
	private String message;
	private ResultDTO result;
	public boolean isSuccess() {
		return success;
	}
	public void setSuccess(boolean success) {
		this.success = success;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public ResultDTO getResult() {
		return result;
	}
	public void setResult(ResultDTO result) {
		this.result = result;
	}

	
}
