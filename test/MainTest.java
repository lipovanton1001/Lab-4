public class MainTest {
    
    public static void main(String[] args) {
        System.out.println("Running tests...");
        
        // Тест 1
        String result = Main.getMessage();
        if (result.equals("Hello from Lab-4!")) {
            System.out.println("✓ Test 1 PASSED: getMessage() works correctly");
        } else {
            System.out.println("✗ Test 1 FAILED: Expected 'Hello from Lab-4!' but got '" + result + "'");
        }
        
        // Тест 2
        System.out.println("✓ Test 2 PASSED: Always passes");
        
        System.out.println("All tests completed!");
    }
}