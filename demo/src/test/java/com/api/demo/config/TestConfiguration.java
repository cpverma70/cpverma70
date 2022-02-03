package com.api.demo.config;

import org.mockito.Mockito;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Profile;

import com.api.demo.impl.ApiServiceImpl;

@Profile("test")
@Configuration
public class TestConfiguration {
	
	@Bean
    @Primary
    public ApiServiceImpl nameService() {
        return Mockito.mock(ApiServiceImpl.class);
    }

}
