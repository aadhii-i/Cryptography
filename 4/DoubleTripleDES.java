import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

public class DoubleTripleDES {

    // DES encryption
    static byte[] encryptDES(byte[] data, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return cipher.doFinal(data);
    }

    // DES decryption
    static byte[] decryptDES(byte[] data, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        return cipher.doFinal(data);
    }

    public static void main(String[] args) throws Exception {

        String plaintext = "HELLO123";

        // Generate two DES keys
        KeyGenerator generator = KeyGenerator.getInstance("DES");

        SecretKey K1 = generator.generateKey();
        SecretKey K2 = generator.generateKey();

        // ---------------- DOUBLE DES ----------------

        byte[] step1 = encryptDES(plaintext.getBytes(), K1);
        byte[] doubleDES = encryptDES(step1, K2);

        // Decrypt Double DES
        byte[] d1 = decryptDES(doubleDES, K2);
        byte[] doubleDecrypted = decryptDES(d1, K1);

        System.out.println("===== DOUBLE DES =====");
        System.out.println("Plaintext : " + plaintext);
        System.out.println("Ciphertext: " +
                Base64.getEncoder().encodeToString(doubleDES));
        System.out.println("Decrypted : " +
                new String(doubleDecrypted));


        // ---------------- TRIPLE DES ----------------

        // EDE: Encrypt K1 → Decrypt K2 → Encrypt K1
        byte[] t1 = encryptDES(plaintext.getBytes(), K1);
        byte[] t2 = decryptDES(t1, K2);
        byte[] tripleDES = encryptDES(t2, K1);

        // Decryption: Decrypt K1 → Encrypt K2 → Decrypt K1
        byte[] td1 = decryptDES(tripleDES, K1);
        byte[] td2 = encryptDES(td1, K2);
        byte[] tripleDecrypted = decryptDES(td2, K1);

        System.out.println("\n===== TRIPLE DES =====");
        System.out.println("Plaintext : " + plaintext);
        System.out.println("Ciphertext: " +
                Base64.getEncoder().encodeToString(tripleDES));
        System.out.println("Decrypted : " +
                new String(tripleDecrypted));
    }
}