from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
# Hase begibt sich auf die Homepage der neuen coolen App

        self.browser.get('http://localhost:8000')

# Hase schaut sich den Titel an 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# Hase kann direkt ein todo Element eintragen

# Hase tippt "Kakao kaufen" in eine Textbox

# Sobald Hase Enter drückt, aktualisiert sich die Seite und es gibt eine Anzeig "1: Kakao kaufen" als erster Punkt auf der to-do Liste

# Es gibt wieder eine Textbox, in welcher Hase einträgt "Kakao zubereiten"

# Die App aktualisiert sich und zeigt beide Einträge

# Hase entdeckt die unique URL und einen erklärenden Text dazu

# Hase besucht diese URL und Ihre Liste ist immernoch dort zu finden

# Hase over and out


if __name__ == '__main__':
    unittest.main(warnings='ignore')







