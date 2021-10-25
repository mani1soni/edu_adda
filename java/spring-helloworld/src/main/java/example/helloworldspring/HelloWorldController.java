package example.helloworldspring;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

/**
 * class for HelloWorldController
 *
 * @author Chandraleka
 *
 */
@Controller
public class HelloWorldController {
  /**
   * method to display message
   *
   * @return string
   */
  @RequestMapping("/welcome")
  public ModelAndView helloWorld() {

    String message = "Hello World from Spring MVC";
    return new ModelAndView("welcome", "message", message);
  }

}
