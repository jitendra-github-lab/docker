package com.springb.dockerapp.dockerdemo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/rest/docker/display")
public class Resource {
	
	@GetMapping
	public String display() {
		return "Displaying message using Spring Boot and Docker...";
	}

}
