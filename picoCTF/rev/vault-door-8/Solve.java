public class Solve {
    public static void main(String[] args) {
        char[] expected = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC1, 0xC0, 0x95, 0x94, 0x94, 0xC1, 0xD1, 0xE1, 0xF1 };

        for (int i=0; i < expected.length; i++) {
            char c = expected[i];
            c = switchBits(c, 6, 7);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 3, 4);
            c = switchBits(c, 0, 1);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 5, 6);
            c = switchBits(c, 0, 3);
            c = switchBits(c, 1, 2);
            expected[i] = c;
        }

        System.out.print("picoCTF{");
        for (int i = 0; i < expected.length; i++) {
            System.out.print(expected[i]);
        }
        System.out.print("}");
    }

    public static char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit that was in position p2 to position p1. Precondition: p1 < p2 */ 
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ 
        char bit1 = (char)(c & mask1); 
        char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ 
        char rest = (char)(c & ~(mask1 | mask2)); 
        char shift = (char)(p2 - p1); 
        char result = (char)((bit1<<shift) | (bit2>>shift) | rest); 
        return result;
    } 
}