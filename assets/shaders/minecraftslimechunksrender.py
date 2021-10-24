import math
import random

def shader(x, y, z):
    seed = math.floor(z)
    px = x*16
    py = y*16
    random.seed(seed + (px * px * 0x4c1906) + (px * 0x5ac0db) + (py * py) * 0x4307a7 + (py * 0x5f24f) ^ 0x3ad8025f)
    color = (random.randint(0, 9) == 0) * 255
    return (0, color, 0)
	
x = """
import java.util.Random; 

public class checkSlimechunk{ 

    public static void main(String args[]) 
    { 
        // the seed from /seed as a 64bit long literal
        long seed = 12345L;
        int xPosition = 123;
        int zPosition = 456;

        Random rnd = new Random(
                seed +
                (int) (xPosition * xPosition * 0x4c1906) +
                (int) (xPosition * 0x5ac0db) +
                (int) (zPosition * zPosition) * 0x4307a7L +
                (int) (zPosition * 0x5f24f) ^ 0x3ad8025fL
        );

        System.out.println(rnd.nextInt(10) == 0);
    } 
}
"""
