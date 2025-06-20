import unittest
from EnigmaEnhanced.core import EnigmaEnhanced

class TestEnigmaEnhanced(unittest.TestCase):
    def setUp(self):
        self.enigma = EnigmaEnhanced()
        self.enigma.generate_key("test_key.json")
        
    def test_encrypt_decrypt(self):
        plaintext = "Hello, World! 你好，世界！"
        encrypted = self.enigma.encrypt(plaintext)
        self.assertTrue(encrypted.startswith("ENC:"))
        
        decrypted = self.enigma.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)
        
    def test_invalid_decrypt(self):
        # 测试无效的密文
        result = self.enigma.decrypt("INVALID:AbCdEfG")
        self.assertTrue("错误" in result or "ERROR" in result)
        
    def test_key_mismatch(self):
        # 测试密钥不匹配
        plaintext = "Test message"
        encrypted = self.enigma.encrypt(plaintext)
        
        # 创建新密钥
        new_enigma = EnigmaEnhanced()
        new_enigma.generate_key("new_key.json")
        
        result = new_enigma.decrypt(encrypted)
        self.assertTrue("密钥不匹配" in result or "Key mismatch" in result)

if __name__ == "__main__":
    unittest.main()
