internal class Program
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            repl();
        }
        else if (args.Length == 1)
        {
            var errors = runFile(args[0]);
            if (errors.Any())
            {
                Environment.Exit(65);
            }
        }
        else
        {
            Console.WriteLine("Usage: lox [script]");
        }
    }

    // Run a lox program file
    private static Error[] runFile(string filepath)
    {
        // Read all the text from the file and run the program
        return run(File.ReadAllText(filepath));
    }

    // Run a lox REPL
    private static void repl()
    {
        // read input from user in infinite loop
        while (true)
        {
            Console.Write("> ");
            var text = Console.ReadLine();

            if (text == null)
            {
                break;
            }

            run(text);
        }
    }

    private static Error[] run(string source)
    {
        // For now, just print the tokens.
        foreach (var token in Scanner.ScanTokens(source)) {
            Console.WriteLine(token);
        }

        return true;
    }
}

internal class Scanner {

    public static Token[] ScanTokens(string source) {
        return new Token[0];
    }
}


internal class Token {
}


internal class Error {
    int line;
    string message;
}
