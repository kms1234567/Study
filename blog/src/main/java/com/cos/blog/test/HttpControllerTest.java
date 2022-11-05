package com.cos.blog.test;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

// 사용자가 요청->응답(HTML 파일) 은 @Controller 어노테이션!

// 사용자가 요청 -> 응답 (Data) 해주는 컨트롤러
@RestController
public class HttpControllerTest {
	
	// 들어오는 값을 해당 객체에 Spring이 알아서 맵핑시켜준다.
	// 인터넷 브라우저 요청은 Get 요청밖에 할 수 없다.
	// http://localhost:8080/http/get (select)
	@GetMapping("/http/get")
	public String getTest(Member m) { // MessageConverter 가 해당 역할을 한다.(스프링부투)
		return "get 요청" + m.getId() + ", " + m.getPassword() + ", " + m.getUsername() + ", " + m.getEmail();
	}
	
	// http://localhost:8080/http/post (insert)
	@PostMapping("/http/post") // MIME type이 application/json으로 날라오면서 Spring은 받은 json 을 Member 객체에 맵핑시킨다.
	public String postTest(@RequestBody Member m) {
		return "post 요청" +m.getId() + ", " + m.getPassword() + ", " + m.getUsername() + ", " + m.getEmail();
	}
	
	// http://localhost:8080/http/put (update)
	@PutMapping("/http/put")
	public String putTest(@RequestBody Member m) {
		return "put 요청" +m.getId() + ", " + m.getPassword() + ", " + m.getUsername() + ", " + m.getEmail();
	}
	
	// http://localhost:8080/http/delete (delete)
	@DeleteMapping("/http/delete")
	public String deleteTest() {
		return "delete 요청";
	}
}