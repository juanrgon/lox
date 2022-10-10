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

        return new Error[0];
    }
}
