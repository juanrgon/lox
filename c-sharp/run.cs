// Run lox code.

// examples:
// Run.file("c-sharp/lox.cs");
// Run.repl();

internal class Run {
    // Run a lox program file
    public static Error[] file(string filepath)
    {
        // Read all the text from the file and run the program
        return run(File.ReadAllText(filepath));
    }

    // Run a lox REPL
    public static void repl()
    {
        // read input from user in infinite loop
        while (true)
        {
            Console.Write("> ");
            var code = Console.ReadLine();

            if (code == null)
            {
                break;
            }

            run(code);
        }
    }

    private static Error[] run(string code)
    {
        // For now, just print the tokens.
        foreach (var token in Scanner.getTokens(code)) {
            Console.WriteLine(token);
        }

        return new Error[0];
    }
}
