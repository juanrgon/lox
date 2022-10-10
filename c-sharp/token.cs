internal class Token {
    public Token(Token.Types type, string lexeme, object literal, int line) {
        this.type = type;
        this.lexeme = lexeme;
        this.literal = literal;
        this.line = line;
    }

    public String asString() {
        return type + " " + lexeme + " " + literal;
    }

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

    public static Dictionary<string, Token.Types> singleCharTokens = new Dictionary<string, Token.Types>() {
        {"(", Token.Types.LEFT_PAREN},
        {")", Token.Types.RIGHT_PAREN},
        {"{", Token.Types.LEFT_BRACE},
        {"}", Token.Types.RIGHT_BRACE},
        {".", Token.Types.DOT},
        {"-", Token.Types.MINUS},
        {"+", Token.Types.PLUS},
        {"*", Token.Types.STAR},
    };

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

}

