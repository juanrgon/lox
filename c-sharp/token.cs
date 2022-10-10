internal class Token {
    Token.Types type;
    string lexeme;
    object? literal;
    int line;

    public enum Types {
      // Single-character tokens.
      LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
      COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,

      // One or two character tokens.
      BANG, BANG_EQUAL,
      EQUAL, EQUAL_EQUAL,
      GREATER, GREATER_EQUAL,
      LESS, LESS_EQUAL,

      // Literals.
      IDENTIFIER, STRING, NUMBER,

      // Keywords.
      AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,
      PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,

      EOF
    }

    public static Dictionary<string, Token.Types> keywords = new Dictionary<string, Token.Types>() {
      {"and", Token.Types.AND},
      {"class", Token.Types.CLASS},
      {"else", Token.Types.ELSE},
      {"false", Token.Types.FALSE},
      {"for", Token.Types.FOR},
      {"fun", Token.Types.FUN},
      {"if", Token.Types.IF},
      {"nil", Token.Types.NIL},
      {"or", Token.Types.OR},
      {"print", Token.Types.PRINT},
      {"return", Token.Types.RETURN},
      {"super", Token.Types.SUPER},
      {"this", Token.Types.THIS},
      {"true", Token.Types.TRUE},
      {"var", Token.Types.VAR},
      {"while", Token.Types.WHILE},
    };

    public Token(Token.Types type, string lexeme, object literal, int line) {
        this.type = type;
        this.lexeme = lexeme;
        this.literal = literal;
        this.line = line;
    }

    public String asString() {
        return type + " " + lexeme + " " + literal;
    }

    public Token[] listFromCode(string source) {
        return new Token[0];
    }

    public static Token matchingSingleCharToken(string c, int line) {
        Token.Types type;

        switch (c) {
            case "(":
                type = Token.Types.LEFT_PAREN;
                break;
            case ")":
                type = Token.Types.RIGHT_PAREN;
                break;
            case "{":
                type = Token.Types.LEFT_BRACE;
                break;
            case "}":
                type = Token.Types.RIGHT_BRACE;
                break;
            case ",":
                type = Token.Types.COMMA;
                break;
            case ".":
                type = Token.Types.DOT;
                break;
            case "-":
                type = Token.Types.MINUS;
                break;
            case "+":
                type = Token.Types.PLUS;
                break;
            case ";":
                type = Token.Types.SEMICOLON;
                break;
            case "*":
                type = Token.Types.STAR;
                break;
            default:
                throw new Exception("Unexpected character: " + c);
        }

        return new Token(type, c, null, line);
    }

    public static Token matchingKeyWordToken(string c, int line) {
        Token.Types type;

        switch (c) {
            case "(":
                type = Token.Types.LEFT_PAREN;
                break;
            case ")":
                type = Token.Types.RIGHT_PAREN;
                break;
            case "{":
                type = Token.Types.LEFT_BRACE;
                break;
            case "}":
                type = Token.Types.RIGHT_BRACE;
                break;
            case ",":
                type = Token.Types.COMMA;
                break;
            case ".":
                type = Token.Types.DOT;
                break;
            case "-":
                type = Token.Types.MINUS;
                break;
            case "+":
                type = Token.Types.PLUS;
                break;
            case ";":
                type = Token.Types.SEMICOLON;
                break;
            case "*":
                type = Token.Types.STAR;
                break;
            default:
                throw new Exception("Unexpected character: " + c);
        }

        return new Token(type, c, null, line);
    }
}

