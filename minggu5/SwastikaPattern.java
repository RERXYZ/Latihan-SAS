public class SwastikaPattern {
    public static void main(String[] args) {
        int n = 7; // size of the swastika (must be odd)

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Top half
                if (i < n / 2) {
                    if (j == n / 2 || j == n - 1 || i == 0) {
                        System.out.print("* ");
                    } else {
                        System.out.print("  ");
                    }
                }
                // Middle row
                else if (i == n / 2) {
                    System.out.print("* ");
                }
                // Bottom half
                else {
                    if (j == 0 || j == n / 2 || i == n - 1) {
                        System.out.print("* ");
                    } else {
                        System.out.print("  ");
                    }
                }
            }
            System.out.println();
        }
    }
}
