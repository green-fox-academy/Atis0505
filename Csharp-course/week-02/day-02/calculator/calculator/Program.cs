using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    class Program
    {
        static void Main()
        {
            // Create a simple calculator application which reads the parameters from the prompt
            // and prints the result to the prompt.
            // It should support the following operations,
            // reate a method named "Calculate()":
            // +, -, *, /, % and it should support two operands.
            // The format of the expressions must be: {operation} {operand} {operand}.
            // Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)
            Console.WriteLine("Please type in the expression:");
            Console.Write("Operation: ");
            var op = Console.ReadLine();
            Console.Write("First number: ");
            var x = Console.ReadLine();
            var xInt = int.Parse(x.ToString());
            Console.Write("Second number: ");
            var y = Console.ReadLine();
            var yInt = int.Parse(y.ToString());

            Console.WriteLine("Result: {0}", Calculator(op, xInt ,yInt));
            Console.ReadKey();
            // You can use the Scanner class
            // It should work like this:

            // Start the program
            // It prints: "Please type in the expression:"
            // Waits for the user input
            // Print the result to the prompt
            // Exit
        }

        public static int Calculator(string oper, int num01, int num02)
        {
            int result = 0;
            switch (oper)
            {
                case "+": result = num01 + num02;
                    break;
                case "-":
                    result = num01 - num02;
                    break;
                case "*":
                    result = num01 * num02;
                    break;
                case "/":
                    result = num01 / num02;
                    break;
            }
            return result;
        }
    }
}
