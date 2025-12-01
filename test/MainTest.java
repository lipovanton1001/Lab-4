import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {
    
    @Test
    public void testGetMessage() {
        String result = Main.getMessage();
        assertEquals("Hello from Lab-4?", result);
    }
    
    @Test
    public void testAlwaysPasses() {
        assertTrue(true);
    }
}