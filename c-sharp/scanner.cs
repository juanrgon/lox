internal class Scanner {
    /**
     * Class for scanning lox code for tokens.
     */

    public static Token[] getTokens(string code) {
        /** Use two-pointers (start and end) to scan the code for tokens.
         *
         *   var mystring = "bar";
         *       ^       ^
         *       s       e
         *       t       n
         *       a       d
         *       r
         *       t
         */

        Scanner scanner = new Scanner(code);
        List<Token> tokens = new List<Token>();
        int line = 1;

        while (true) {
            switch(scanner.lexeme()) {
                case "\n":
                    line++;
                    break;
                case "/":
                    if (scanner.match("/")) {
                        // A comment goes until the end of the line.
                        while (scanner.lookahead() != "\n" && !scanner.atEnd()) scanner.advance();
                    } else {
                        tokens.Add(new Token(Token.Types.SLASH, scanner.lexeme(), null, line));
                    }
                    break;
                case "(":
                case ")":
                case "{":
                case "}":
                case ",":
                case ".":
                case "-":
                case "+":
                case ";":
                case "*":
                    tokens.Add(Token.matchingSingleCharToken(scanner.lexeme(), line));
                    break;
                case "!":
                    tokens.Add(new Token(scanner.match("=") ? Token.Types.BANG_EQUAL: Token.Types.BANG, scanner.lexeme(), null, line));
                    break;
                case "=":
                    tokens.Add(new Token((scanner.match("=")) ? Token.Types.EQUAL_EQUAL: Token.Types.EQUAL, scanner.lexeme(), null, line));
                    break;
                case ">":
                    tokens.Add(new Token(scanner.match("=") ? Token.Types.GREATER_EQUAL: Token.Types.GREATER, scanner.lexeme(), null, line));
                    break;
                case "<":
                    tokens.Add(new Token(scanner.match("=") ? Token.Types.LESS_EQUAL : Token.Types.LESS, scanner.lexeme(), null, line));
                    break;
                case "'":
                case "\"":
                    var quote = scanner.lexeme();
                    var token_type = Token.Types.STRING;

                    while (scanner.lookahead() != quote && !scanner.atEnd()) {
                        if (scanner.lookahead() == "\n") line++;
                        scanner.advance();
                    }
                    break;
                default:
                    if (scanner.isDigit(scanner.lexeme())) {
                        while (scanner.isDigit(scanner.lexeme())) scanner.advance();

                        // Look for a fractional part.
                        if (scanner.lookahead() == "." && scanner.isDigit(scanner.lookahead(2))) {
                            // Consume the "."
                            scanner.advance();

                            while (scanner.isDigit(scanner.lexeme())) scanner.advance();
                        }

                        tokens.Add(new Token(Token.Types.NUMBER, scanner.lexeme(), Double.Parse(scanner.lexeme()), line));
                    }

                    else if (scanner.isAlpha(scanner.lexeme())) {
                        while (scanner.isAlphaNumeric(scanner.lexeme())) scanner.advance();

                        // See if the identifier is a keyword.
                        var word = scanner.lexeme();
                        var type = Token.Types.IDENTIFIER;

                        if (Token.keywords.ContainsKey(word)) {
                            type = Token.keywords[word];
                        }

                        tokens.Add(new Token(type, word, null, line));
                    }
                    break;
            }
        }

        tokens.Add(new Token(Token.Types.EOF, "", null, line));

        return tokens.ToArray();
    }

    private string code;
    private int start = 0;
    private int end = 1;

    private Scanner(string code) {
        this.code = code;
    }


    private void advance(int amount = 1) {
        this.end += amount;
    }

    private string consume() {
        var lexeme = this.lexeme();
        (this.start, this.end) = (this.end, this.end + 1);
        return lexeme;
    }

    private string lexeme() {
        return this.code.Substring(this.start, this.end);
    }

    private string lookahead(int amount = 1) {
        return this.code.Substring(this.end, this.end + amount);
    }

    private bool match(string target) {
        if (this.lookahead(target.Length) == target) {
            this.advance();
            return true;
        }
        return false;
    }

    private void retreat() {
        this.end--;
    }

    private bool atEnd() {
        return this.end > this.code.Length;
    }

    private bool isDigit(string c) {
        return "0123456789".Contains(c[0]);
    }

    private bool isAlpha(string c) {
        return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_".Contains(c[0]);
    }

    private bool isAlphaNumeric(string c) {
        return this.isAlpha(c) || this.isDigit(c);
    }
}
