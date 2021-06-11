import unittest
import main

class Tests(unittest.TestCase):
    # All tests were written first before the implementation
    # All tests were failing at the beginning
    # Goal is to fix all of the tests, in compliance with the requirements, by tweaking the implementation

    """
    | Write a method greet(name) that interpolates name in a simple greeting.
    | For example, when name is "Bob", the method should return a string "Hello, Bob.".

    | Given: an input: {name}
    | When: the greet function is called with the given input
    | Then: function should return string: Hello, {name}.
    """
    def test_simple_greeting(self):
        name = 'Bob'
        expectation = 'Hello, {}.'.format(name)
        actual = main.greet(name)
        self.assertEqual(expectation, actual)

    """
      | Handle nulls by introducing a stand-in. For example, when name is null, 
      | then the method should return the string "Hello, my friend."
      
      | Given: an input: None/null
      | When: the greet function is called with the given input
      | Then: function should swallow null and return a generic text string: Hello, my friend.
    """
    def test_null_case(self):
        name = None
        expectation = 'Hello, my friend.'

        actual = main.greet(name)
        self.assertEqual(expectation, actual)

    def test_empty_string_case(self):
        name = None
        expectation = 'Hello, my friend.'

        actual = main.greet(name)
        self.assertEqual(expectation, actual)
    """
      | Handle shouting. When name is all uppercase, then the method should shout back to the user. 
      | For example, when name is "JERRY" then the method should return the string "HELLO JERRY!"
      
      | Given: an uppercase input: {name}
      | When: the greet function is called with the given input
      | Then: function should return string: HELLO {name}!
    """
    def test_single_uppercase(self):
        name = 'JERRY'
        expectation = 'HELLO {}!'.format(name)
        actual = main.greet(name)
        self.assertEqual(expectation, actual)

    """
      | Handle two names of input. 
      | When name is an array of two names (or, in languages that support it, varargs or a splat), 
      | then both names should be printed. For example, when name is ["Jill", "Jane"], 
      | then the method should return the string "Hello, Jill and Jane."

      | Given: an input array with two names: [{name1}, {name2}]
      | When: the greet function is called with the given input
      | Then: function should return string: Hello, {name1} and {name2}.
    """
    def test_two_inputs(self):
        name = ['Jill', 'Jane']
        expectation = 'Hello, {} and {}.'.format(name[0], name[1])

        actual = main.greet(name)
        self.assertEqual(expectation, actual)

    """
      | Handle an arbitrary number of names as input. 
      | When name represents more than two names, separate them with commas
      | and close with an Oxford comma and "and". For example, when name is ["Amy", "Brian", "Charlotte"], 
      | then the method should return the string "Hello, Amy, Brian, and Charlotte."
        
        
      | Given: an input array with three names: [{name1}, {name2}, {name3}]
      | When: the greet function is called with the given input
      | Then: function should return string: Hello, {name1}, {name2}, and {name3}.
      """
    def test_arbitary_inputs(self):
        names = ["Amy", "Brian", "Charlotte"]
        expectation = "Hello, Amy, Brian, and Charlotte."

        actual = main.greet(names)
        self.assertEqual(expectation, actual)

    """
      | Allow mixing of normal and shouted names by separating the response into two greetings. 
      | For example, when name is ["Amy", "BRIAN", "Charlotte"], 
      | then the method should return the string "Hello, Amy and Charlotte. AND HELLO BRIAN!"


      | Given: an input array with three mixed-case names: [{name1}, {UPPERCASE_NAME}, {name3}]
      | When: the greet function is called with the given input
      | Then: function should return string: Hello, {name1} and {name2}. AND HELLO {UPPERCASE_NAME}!
      """
    def test_arbitary_mixed_inputs(self):
        names = ["Amy", "BRIAN", "Charlotte"]
        expectation = "Hello, Amy and Charlotte. AND HELLO BRIAN!"

        actual = main.greet(names)
        self.assertEqual(expectation, actual)

    """
      | If any entries in name are a string containing a comma, split it as its own input. 
      | For example, when name is ["Bob", "Charlie, Dianne"], 
      | then the method should return the string "Hello, Bob, Charlie, and Dianne.".

      | Given: an input string that contains array with comma separated values: [{name1}, {name2}, {name3}"]
      | When: the greet function is called with the given input
      | Then: function should return string: Hello, {name1}, {name2}, and {name3}.
      """
    def test_array_as_string(self):
        names = ["Bob", "Charlie, Dianne"]
        expectation = 'Hello, Bob, Charlie, and Dianne.'

        actual = main.greet(names)
        self.assertEqual(expectation, actual)

    """
       | Allow the input to escape intentional commas introduced by Requirement 7. 
       | These can be escaped in the same manner that CSV is, 
       | with double quotes surrounding the entry. 
       | For example, when name is ["Bob", "\"Charlie, Dianne\""], 
       | then the method should return the string "Hello, Bob and Charlie, Dianne.".

       | Given: an input string that contains array with escaped comma separated values:  [{name1}", "\"{name2}, {name3}\""]
       | When: the greet function is called with the given input
       | Then: function should return string: Hello, {name1} and {name2}, {name3}.
       """
    def test_array_as_string_escaped(self):
        names = ["Bob", "\"Charlie, Dianne\""]
        expectation = "Hello, Bob and Charlie, Dianne."

        actual = main.greet(names)
        self.assertEqual(expectation, actual)

    # Negative case, where input is some integer
    def test_illegal_argument(self):
        name = 1
        self.assertRaises(ValueError, main.greet, name)


if __name__ == '__main__':
    unittest.main()
