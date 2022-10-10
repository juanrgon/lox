internal class Lox
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Run.repl();
        }
        else if (args.Length == 1)
        {
            var errors = Run.file(args[0]);
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

}
