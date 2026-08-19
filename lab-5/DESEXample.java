import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

public class DESExample {

    public static void main(String[] args) throws Exception {

        // Generate DES key
        KeyGenerator keyGenerator = KeyGenerator.getInstance("DES");
        SecretKey key = keyGenerator.generateKey();

        String plaintext = "HELLO123";

        // Encryption
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);

        byte[] encrypted = cipher.doFinal(plaintext.getBytes());

        // Decryption
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(encrypted);

        System.out.println("Plaintext : " + plaintext);
        System.out.println("Key       : " +
                Base64.getEncoder().encodeToString(key.getEncoded()));
        System.out.println("Encrypted : " +
                Base64.getEncoder().encodeToString(encrypted));
        System.out.println("Decrypted : " + new String(decrypted));
    }
}
