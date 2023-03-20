// Generated from /Users/noah/Documents/School/universiteit/2Ba Informatica/Compilers/compilers-project/src/grammar/C.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		AUTO=1, BREAK=2, CASE=3, CHAR=4, CONST=5, CONTINUE=6, DEFAULT=7, DO=8, 
		DOUBLE=9, ELSE=10, ENUM=11, EXTERN=12, FLOAT=13, FOR=14, GOTO=15, IF=16, 
		INT=17, LONG=18, REGISTER=19, RETURN=20, SHORT=21, SIGNED=22, SIZEOF=23, 
		STATIC=24, STRUCT=25, SWITCH=26, TYPEDEF=27, UNION=28, UNSIGNED=29, VOID=30, 
		VOLATILE=31, WHILE=32, ASSIGN_OP=33, PLUS_ASSIGN_OP=34, MINUS_ASSIGN_OP=35, 
		STAR_ASSIGN_OP=36, SLASH_ASSIGN_OP=37, PERCENT_ASSIGN_OP=38, AMPERSAND_ASSIGN_OP=39, 
		BAR_ASSIGN_OP=40, CARET_ASSIGN_OP=41, SHIFTL_ASSIGN_OP=42, SHIFTR_ASSING_OP=43, 
		INCREMENT_OP=44, DECREMENT_OP=45, PLUS_OP=46, MINUS_OP=47, STAR_OP=48, 
		SLASH_OP=49, PERCENT_OP=50, TILDE_OP=51, AMPERSAND_OP=52, BAR_OP=53, CARET_OP=54, 
		SHIFTL_OP=55, SHIFTR_OP=56, NOT_OP=57, AND_OP=58, OR_OP=59, EQ_OP=60, 
		NEQ_OP=61, LT_OP=62, LE_OP=63, GT_OP=64, GE_OP=65, DOT_OP=66, ARROW_OP=67, 
		QUESTION_OP=68, LPAREN=69, RPAREN=70, LBRACKET=71, RBRACKET=72, LBRACE=73, 
		RBRACE=74, COLON=75, SEMICOLON=76, COMMA=77, INT_LITERAL=78, REAL_LITERAL=79, 
		CHAR_LITERAL=80, STRING_LITERAL=81, IDENTIFIER=82, INCLUDE=83, PATH=84, 
		COMMENT=85, LINE_COMMENT=86, WS=87;
	public static final int
		RULE_start = 0, RULE_function_declaration = 1, RULE_function_parameter = 2, 
		RULE_return_type = 3, RULE_macro = 4, RULE_statement = 5, RULE_compound_statement = 6, 
		RULE_selection_statement = 7, RULE_iteration_statement = 8, RULE_jump_statement = 9, 
		RULE_expression = 10, RULE_literal = 11, RULE_variable = 12, RULE_type_specifier = 13, 
		RULE_declaration = 14, RULE_declarator = 15, RULE_function_call = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "function_declaration", "function_parameter", "return_type", 
			"macro", "statement", "compound_statement", "selection_statement", "iteration_statement", 
			"jump_statement", "expression", "literal", "variable", "type_specifier", 
			"declaration", "declarator", "function_call"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'auto'", "'break'", "'case'", "'char'", "'const'", "'continue'", 
			"'default'", "'do'", "'double'", "'else'", "'enum'", "'extern'", "'float'", 
			"'for'", "'goto'", "'if'", "'int'", "'long'", "'register'", "'return'", 
			"'short'", "'signed'", "'sizeof'", "'static'", "'struct'", "'switch'", 
			"'typedef'", "'union'", "'unsigned'", "'void'", "'volatile'", "'while'", 
			"'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", "'|='", "'^='", 
			"'<<='", "'>>='", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'~'", "'&'", "'|'", "'^'", "'<<'", "'>>'", "'!'", "'&&'", "'||'", "'=='", 
			"'!='", "'<'", "'<='", "'>'", "'>='", "'.'", "'->'", "'?'", "'('", "')'", 
			"'['", "']'", "'{'", "'}'", "':'", "';'", "','", null, null, null, null, 
			null, "'#include'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "AUTO", "BREAK", "CASE", "CHAR", "CONST", "CONTINUE", "DEFAULT", 
			"DO", "DOUBLE", "ELSE", "ENUM", "EXTERN", "FLOAT", "FOR", "GOTO", "IF", 
			"INT", "LONG", "REGISTER", "RETURN", "SHORT", "SIGNED", "SIZEOF", "STATIC", 
			"STRUCT", "SWITCH", "TYPEDEF", "UNION", "UNSIGNED", "VOID", "VOLATILE", 
			"WHILE", "ASSIGN_OP", "PLUS_ASSIGN_OP", "MINUS_ASSIGN_OP", "STAR_ASSIGN_OP", 
			"SLASH_ASSIGN_OP", "PERCENT_ASSIGN_OP", "AMPERSAND_ASSIGN_OP", "BAR_ASSIGN_OP", 
			"CARET_ASSIGN_OP", "SHIFTL_ASSIGN_OP", "SHIFTR_ASSING_OP", "INCREMENT_OP", 
			"DECREMENT_OP", "PLUS_OP", "MINUS_OP", "STAR_OP", "SLASH_OP", "PERCENT_OP", 
			"TILDE_OP", "AMPERSAND_OP", "BAR_OP", "CARET_OP", "SHIFTL_OP", "SHIFTR_OP", 
			"NOT_OP", "AND_OP", "OR_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LE_OP", "GT_OP", 
			"GE_OP", "DOT_OP", "ARROW_OP", "QUESTION_OP", "LPAREN", "RPAREN", "LBRACKET", 
			"RBRACKET", "LBRACE", "RBRACE", "COLON", "SEMICOLON", "COMMA", "INT_LITERAL", 
			"REAL_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", "IDENTIFIER", "INCLUDE", 
			"PATH", "COMMENT", "LINE_COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "C.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public List<Function_declarationContext> function_declaration() {
			return getRuleContexts(Function_declarationContext.class);
		}
		public Function_declarationContext function_declaration(int i) {
			return getRuleContext(Function_declarationContext.class,i);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CParser.SEMICOLON, i);
		}
		public List<MacroContext> macro() {
			return getRuleContexts(MacroContext.class);
		}
		public MacroContext macro(int i) {
			return getRuleContext(MacroContext.class,i);
		}
		public List<Compound_statementContext> compound_statement() {
			return getRuleContexts(Compound_statementContext.class);
		}
		public Compound_statementContext compound_statement(int i) {
			return getRuleContext(Compound_statementContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << CONST) | (1L << FLOAT) | (1L << INT) | (1L << VOID))) != 0) || _la==INCLUDE) {
				{
				setState(43);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(34);
					function_declaration();
					setState(37);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SEMICOLON:
						{
						setState(35);
						match(SEMICOLON);
						}
						break;
					case LBRACE:
						{
						setState(36);
						compound_statement();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				case 2:
					{
					setState(39);
					declaration();
					setState(40);
					match(SEMICOLON);
					}
					break;
				case 3:
					{
					setState(42);
					macro();
					}
					break;
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(CParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(CParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CParser.RPAREN, 0); }
		public List<Function_parameterContext> function_parameter() {
			return getRuleContexts(Function_parameterContext.class);
		}
		public Function_parameterContext function_parameter(int i) {
			return getRuleContext(Function_parameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CParser.COMMA, i);
		}
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			return_type();
			setState(49);
			match(IDENTIFIER);
			setState(50);
			match(LPAREN);
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << CONST) | (1L << FLOAT) | (1L << INT))) != 0)) {
				{
				setState(51);
				function_parameter();
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(52);
					match(COMMA);
					setState(53);
					function_parameter();
					}
					}
					setState(58);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(61);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_parameterContext extends ParserRuleContext {
		public Type_specifierContext type_specifier() {
			return getRuleContext(Type_specifierContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(CParser.IDENTIFIER, 0); }
		public TerminalNode STAR_OP() { return getToken(CParser.STAR_OP, 0); }
		public TerminalNode CONST() { return getToken(CParser.CONST, 0); }
		public Function_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_parameter; }
	}

	public final Function_parameterContext function_parameter() throws RecognitionException {
		Function_parameterContext _localctx = new Function_parameterContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			type_specifier();
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STAR_OP) {
				{
				setState(64);
				match(STAR_OP);
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==CONST) {
					{
					setState(65);
					match(CONST);
					}
				}

				}
			}

			setState(70);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_typeContext extends ParserRuleContext {
		public TerminalNode FLOAT() { return getToken(CParser.FLOAT, 0); }
		public TerminalNode INT() { return getToken(CParser.INT, 0); }
		public TerminalNode CHAR() { return getToken(CParser.CHAR, 0); }
		public TerminalNode STAR_OP() { return getToken(CParser.STAR_OP, 0); }
		public TerminalNode VOID() { return getToken(CParser.VOID, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_return_type);
		int _la;
		try {
			setState(77);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR:
			case FLOAT:
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(72);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << FLOAT) | (1L << INT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==STAR_OP) {
					{
					setState(73);
					match(STAR_OP);
					}
				}

				}
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(76);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MacroContext extends ParserRuleContext {
		public TerminalNode INCLUDE() { return getToken(CParser.INCLUDE, 0); }
		public TerminalNode LT_OP() { return getToken(CParser.LT_OP, 0); }
		public TerminalNode PATH() { return getToken(CParser.PATH, 0); }
		public TerminalNode GT_OP() { return getToken(CParser.GT_OP, 0); }
		public MacroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro; }
	}

	public final MacroContext macro() throws RecognitionException {
		MacroContext _localctx = new MacroContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_macro);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(INCLUDE);
			setState(80);
			match(LT_OP);
			setState(81);
			match(PATH);
			setState(82);
			match(GT_OP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Compound_statementContext compound_statement() {
			return getRuleContext(Compound_statementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(CParser.SEMICOLON, 0); }
		public Selection_statementContext selection_statement() {
			return getRuleContext(Selection_statementContext.class,0);
		}
		public Iteration_statementContext iteration_statement() {
			return getRuleContext(Iteration_statementContext.class,0);
		}
		public Jump_statementContext jump_statement() {
			return getRuleContext(Jump_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_statement);
		try {
			setState(91);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LBRACE:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				compound_statement();
				}
				break;
			case INCREMENT_OP:
			case DECREMENT_OP:
			case PLUS_OP:
			case MINUS_OP:
			case STAR_OP:
			case AMPERSAND_OP:
			case NOT_OP:
			case LPAREN:
			case INT_LITERAL:
			case REAL_LITERAL:
			case CHAR_LITERAL:
			case STRING_LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				expression(0);
				setState(86);
				match(SEMICOLON);
				}
				break;
			case IF:
			case SWITCH:
				enterOuterAlt(_localctx, 3);
				{
				setState(88);
				selection_statement();
				}
				break;
			case DO:
			case FOR:
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(89);
				iteration_statement();
				}
				break;
			case BREAK:
			case CONTINUE:
			case RETURN:
				enterOuterAlt(_localctx, 5);
				{
				setState(90);
				jump_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Compound_statementContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(CParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CParser.SEMICOLON, i);
		}
		public Compound_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_statement; }
	}

	public final Compound_statementContext compound_statement() throws RecognitionException {
		Compound_statementContext _localctx = new Compound_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_compound_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(LBRACE);
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BREAK) | (1L << CHAR) | (1L << CONST) | (1L << CONTINUE) | (1L << DO) | (1L << FLOAT) | (1L << FOR) | (1L << IF) | (1L << INT) | (1L << RETURN) | (1L << SWITCH) | (1L << WHILE) | (1L << INCREMENT_OP) | (1L << DECREMENT_OP) | (1L << PLUS_OP) | (1L << MINUS_OP) | (1L << STAR_OP) | (1L << AMPERSAND_OP) | (1L << NOT_OP))) != 0) || ((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & ((1L << (LPAREN - 69)) | (1L << (LBRACE - 69)) | (1L << (INT_LITERAL - 69)) | (1L << (REAL_LITERAL - 69)) | (1L << (CHAR_LITERAL - 69)) | (1L << (STRING_LITERAL - 69)) | (1L << (IDENTIFIER - 69)))) != 0)) {
				{
				setState(98);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BREAK:
				case CONTINUE:
				case DO:
				case FOR:
				case IF:
				case RETURN:
				case SWITCH:
				case WHILE:
				case INCREMENT_OP:
				case DECREMENT_OP:
				case PLUS_OP:
				case MINUS_OP:
				case STAR_OP:
				case AMPERSAND_OP:
				case NOT_OP:
				case LPAREN:
				case LBRACE:
				case INT_LITERAL:
				case REAL_LITERAL:
				case CHAR_LITERAL:
				case STRING_LITERAL:
				case IDENTIFIER:
					{
					setState(94);
					statement();
					}
					break;
				case CHAR:
				case CONST:
				case FLOAT:
				case INT:
					{
					setState(95);
					declaration();
					setState(96);
					match(SEMICOLON);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(103);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selection_statementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(CParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(CParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(CParser.ELSE, 0); }
		public TerminalNode SWITCH() { return getToken(CParser.SWITCH, 0); }
		public Selection_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selection_statement; }
	}

	public final Selection_statementContext selection_statement() throws RecognitionException {
		Selection_statementContext _localctx = new Selection_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_selection_statement);
		try {
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				match(IF);
				setState(106);
				match(LPAREN);
				setState(107);
				expression(0);
				setState(108);
				match(RPAREN);
				setState(109);
				statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				match(IF);
				setState(112);
				match(LPAREN);
				setState(113);
				expression(0);
				setState(114);
				match(RPAREN);
				setState(115);
				statement();
				setState(116);
				match(ELSE);
				setState(117);
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(119);
				match(SWITCH);
				setState(120);
				match(LPAREN);
				setState(121);
				expression(0);
				setState(122);
				match(RPAREN);
				setState(123);
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Iteration_statementContext extends ParserRuleContext {
		public DeclarationContext init;
		public ExpressionContext cond;
		public ExpressionContext iteration;
		public TerminalNode WHILE() { return getToken(CParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(CParser.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(CParser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode DO() { return getToken(CParser.DO, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(CParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CParser.SEMICOLON, i);
		}
		public TerminalNode FOR() { return getToken(CParser.FOR, 0); }
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public Iteration_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iteration_statement; }
	}

	public final Iteration_statementContext iteration_statement() throws RecognitionException {
		Iteration_statementContext _localctx = new Iteration_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_iteration_statement);
		int _la;
		try {
			setState(156);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHILE:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				match(WHILE);
				setState(128);
				match(LPAREN);
				setState(129);
				expression(0);
				setState(130);
				match(RPAREN);
				setState(131);
				statement();
				}
				break;
			case DO:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				match(DO);
				setState(134);
				statement();
				setState(135);
				match(WHILE);
				setState(136);
				match(LPAREN);
				setState(137);
				expression(0);
				setState(138);
				match(RPAREN);
				setState(139);
				match(SEMICOLON);
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(141);
				match(FOR);
				setState(142);
				match(LPAREN);
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << CONST) | (1L << FLOAT) | (1L << INT))) != 0)) {
					{
					setState(143);
					((Iteration_statementContext)_localctx).init = declaration();
					}
				}

				setState(146);
				match(SEMICOLON);
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 44)) & ~0x3f) == 0 && ((1L << (_la - 44)) & ((1L << (INCREMENT_OP - 44)) | (1L << (DECREMENT_OP - 44)) | (1L << (PLUS_OP - 44)) | (1L << (MINUS_OP - 44)) | (1L << (STAR_OP - 44)) | (1L << (AMPERSAND_OP - 44)) | (1L << (NOT_OP - 44)) | (1L << (LPAREN - 44)) | (1L << (INT_LITERAL - 44)) | (1L << (REAL_LITERAL - 44)) | (1L << (CHAR_LITERAL - 44)) | (1L << (STRING_LITERAL - 44)) | (1L << (IDENTIFIER - 44)))) != 0)) {
					{
					setState(147);
					((Iteration_statementContext)_localctx).cond = expression(0);
					}
				}

				setState(150);
				match(SEMICOLON);
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 44)) & ~0x3f) == 0 && ((1L << (_la - 44)) & ((1L << (INCREMENT_OP - 44)) | (1L << (DECREMENT_OP - 44)) | (1L << (PLUS_OP - 44)) | (1L << (MINUS_OP - 44)) | (1L << (STAR_OP - 44)) | (1L << (AMPERSAND_OP - 44)) | (1L << (NOT_OP - 44)) | (1L << (LPAREN - 44)) | (1L << (INT_LITERAL - 44)) | (1L << (REAL_LITERAL - 44)) | (1L << (CHAR_LITERAL - 44)) | (1L << (STRING_LITERAL - 44)) | (1L << (IDENTIFIER - 44)))) != 0)) {
					{
					setState(151);
					((Iteration_statementContext)_localctx).iteration = expression(0);
					}
				}

				setState(154);
				match(RPAREN);
				setState(155);
				statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Jump_statementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(CParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(CParser.SEMICOLON, 0); }
		public TerminalNode CONTINUE() { return getToken(CParser.CONTINUE, 0); }
		public TerminalNode RETURN() { return getToken(CParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Jump_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jump_statement; }
	}

	public final Jump_statementContext jump_statement() throws RecognitionException {
		Jump_statementContext _localctx = new Jump_statementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_jump_statement);
		int _la;
		try {
			setState(167);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BREAK:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				match(BREAK);
				setState(159);
				match(SEMICOLON);
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				match(CONTINUE);
				setState(161);
				match(SEMICOLON);
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				match(RETURN);
				setState(164);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 44)) & ~0x3f) == 0 && ((1L << (_la - 44)) & ((1L << (INCREMENT_OP - 44)) | (1L << (DECREMENT_OP - 44)) | (1L << (PLUS_OP - 44)) | (1L << (MINUS_OP - 44)) | (1L << (STAR_OP - 44)) | (1L << (AMPERSAND_OP - 44)) | (1L << (NOT_OP - 44)) | (1L << (LPAREN - 44)) | (1L << (INT_LITERAL - 44)) | (1L << (REAL_LITERAL - 44)) | (1L << (CHAR_LITERAL - 44)) | (1L << (STRING_LITERAL - 44)) | (1L << (IDENTIFIER - 44)))) != 0)) {
					{
					setState(163);
					expression(0);
					}
				}

				setState(166);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Token op;
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS_OP() { return getToken(CParser.PLUS_OP, 0); }
		public TerminalNode MINUS_OP() { return getToken(CParser.MINUS_OP, 0); }
		public TerminalNode STAR_OP() { return getToken(CParser.STAR_OP, 0); }
		public TerminalNode AMPERSAND_OP() { return getToken(CParser.AMPERSAND_OP, 0); }
		public TerminalNode NOT_OP() { return getToken(CParser.NOT_OP, 0); }
		public TerminalNode INCREMENT_OP() { return getToken(CParser.INCREMENT_OP, 0); }
		public TerminalNode DECREMENT_OP() { return getToken(CParser.DECREMENT_OP, 0); }
		public TerminalNode LPAREN() { return getToken(CParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CParser.RPAREN, 0); }
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode SLASH_OP() { return getToken(CParser.SLASH_OP, 0); }
		public TerminalNode PERCENT_OP() { return getToken(CParser.PERCENT_OP, 0); }
		public TerminalNode LT_OP() { return getToken(CParser.LT_OP, 0); }
		public TerminalNode LE_OP() { return getToken(CParser.LE_OP, 0); }
		public TerminalNode GT_OP() { return getToken(CParser.GT_OP, 0); }
		public TerminalNode GE_OP() { return getToken(CParser.GE_OP, 0); }
		public TerminalNode EQ_OP() { return getToken(CParser.EQ_OP, 0); }
		public TerminalNode NEQ_OP() { return getToken(CParser.NEQ_OP, 0); }
		public TerminalNode AND_OP() { return getToken(CParser.AND_OP, 0); }
		public TerminalNode OR_OP() { return getToken(CParser.OR_OP, 0); }
		public TerminalNode ASSIGN_OP() { return getToken(CParser.ASSIGN_OP, 0); }
		public TerminalNode PLUS_ASSIGN_OP() { return getToken(CParser.PLUS_ASSIGN_OP, 0); }
		public TerminalNode MINUS_ASSIGN_OP() { return getToken(CParser.MINUS_ASSIGN_OP, 0); }
		public TerminalNode STAR_ASSIGN_OP() { return getToken(CParser.STAR_ASSIGN_OP, 0); }
		public TerminalNode SLASH_ASSIGN_OP() { return getToken(CParser.SLASH_ASSIGN_OP, 0); }
		public TerminalNode PERCENT_ASSIGN_OP() { return getToken(CParser.PERCENT_ASSIGN_OP, 0); }
		public TerminalNode SHIFTL_ASSIGN_OP() { return getToken(CParser.SHIFTL_ASSIGN_OP, 0); }
		public TerminalNode SHIFTR_ASSING_OP() { return getToken(CParser.SHIFTR_ASSING_OP, 0); }
		public TerminalNode AMPERSAND_ASSIGN_OP() { return getToken(CParser.AMPERSAND_ASSIGN_OP, 0); }
		public TerminalNode CARET_ASSIGN_OP() { return getToken(CParser.CARET_ASSIGN_OP, 0); }
		public TerminalNode BAR_ASSIGN_OP() { return getToken(CParser.BAR_ASSIGN_OP, 0); }
		public TerminalNode RBRACKET() { return getToken(CParser.RBRACKET, 0); }
		public TerminalNode LBRACKET() { return getToken(CParser.LBRACKET, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(170);
				function_call();
				}
				break;
			case 2:
				{
				setState(171);
				((ExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INCREMENT_OP) | (1L << DECREMENT_OP) | (1L << PLUS_OP) | (1L << MINUS_OP) | (1L << STAR_OP) | (1L << AMPERSAND_OP) | (1L << NOT_OP))) != 0)) ) {
					((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(172);
				expression(11);
				}
				break;
			case 3:
				{
				setState(173);
				match(LPAREN);
				setState(174);
				expression(0);
				setState(175);
				match(RPAREN);
				}
				break;
			case 4:
				{
				setState(177);
				variable();
				}
				break;
			case 5:
				{
				setState(178);
				literal();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(211);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(209);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(181);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(182);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR_OP) | (1L << SLASH_OP) | (1L << PERCENT_OP))) != 0)) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(183);
						expression(11);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(184);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(185);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS_OP || _la==MINUS_OP) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(186);
						expression(10);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(187);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(188);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(((((_la - 62)) & ~0x3f) == 0 && ((1L << (_la - 62)) & ((1L << (LT_OP - 62)) | (1L << (LE_OP - 62)) | (1L << (GT_OP - 62)) | (1L << (GE_OP - 62)))) != 0)) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(189);
						expression(9);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(190);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(191);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==EQ_OP || _la==NEQ_OP) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(192);
						expression(8);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(193);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(194);
						((ExpressionContext)_localctx).op = match(AND_OP);
						setState(195);
						expression(7);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(196);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(197);
						((ExpressionContext)_localctx).op = match(OR_OP);
						setState(198);
						expression(6);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(199);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(200);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ASSIGN_OP) | (1L << PLUS_ASSIGN_OP) | (1L << MINUS_ASSIGN_OP) | (1L << STAR_ASSIGN_OP) | (1L << SLASH_ASSIGN_OP) | (1L << PERCENT_ASSIGN_OP) | (1L << AMPERSAND_ASSIGN_OP) | (1L << BAR_ASSIGN_OP) | (1L << CARET_ASSIGN_OP) | (1L << SHIFTL_ASSIGN_OP) | (1L << SHIFTR_ASSING_OP))) != 0)) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(201);
						expression(4);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(202);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(203);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==INCREMENT_OP || _la==DECREMENT_OP) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(204);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(205);
						((ExpressionContext)_localctx).op = match(LBRACKET);
						setState(206);
						expression(0);
						setState(207);
						match(RBRACKET);
						}
						break;
					}
					} 
				}
				setState(213);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	 
		public LiteralContext() { }
		public void copyFrom(LiteralContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StringContext extends LiteralContext {
		public TerminalNode STRING_LITERAL() { return getToken(CParser.STRING_LITERAL, 0); }
		public StringContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class CharContext extends LiteralContext {
		public TerminalNode CHAR_LITERAL() { return getToken(CParser.CHAR_LITERAL, 0); }
		public CharContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class RealContext extends LiteralContext {
		public TerminalNode REAL_LITERAL() { return getToken(CParser.REAL_LITERAL, 0); }
		public RealContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends LiteralContext {
		public TerminalNode INT_LITERAL() { return getToken(CParser.INT_LITERAL, 0); }
		public IntContext(LiteralContext ctx) { copyFrom(ctx); }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_literal);
		try {
			setState(218);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR_LITERAL:
				_localctx = new CharContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(214);
				match(CHAR_LITERAL);
				}
				break;
			case STRING_LITERAL:
				_localctx = new StringContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				match(STRING_LITERAL);
				}
				break;
			case INT_LITERAL:
				_localctx = new IntContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(216);
				match(INT_LITERAL);
				}
				break;
			case REAL_LITERAL:
				_localctx = new RealContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(217);
				match(REAL_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(CParser.IDENTIFIER, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_specifierContext extends ParserRuleContext {
		public TerminalNode FLOAT() { return getToken(CParser.FLOAT, 0); }
		public TerminalNode INT() { return getToken(CParser.INT, 0); }
		public TerminalNode CHAR() { return getToken(CParser.CHAR, 0); }
		public List<TerminalNode> CONST() { return getTokens(CParser.CONST); }
		public TerminalNode CONST(int i) {
			return getToken(CParser.CONST, i);
		}
		public Type_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_specifier; }
	}

	public final Type_specifierContext type_specifier() throws RecognitionException {
		Type_specifierContext _localctx = new Type_specifierContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_type_specifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONST) {
				{
				setState(222);
				match(CONST);
				}
			}

			setState(225);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << FLOAT) | (1L << INT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONST) {
				{
				setState(226);
				match(CONST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public Type_specifierContext type_specifier() {
			return getRuleContext(Type_specifierContext.class,0);
		}
		public List<DeclaratorContext> declarator() {
			return getRuleContexts(DeclaratorContext.class);
		}
		public DeclaratorContext declarator(int i) {
			return getRuleContext(DeclaratorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CParser.COMMA, i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			type_specifier();
			setState(230);
			declarator();
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(231);
				match(COMMA);
				setState(232);
				declarator();
				}
				}
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclaratorContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(CParser.IDENTIFIER, 0); }
		public List<TerminalNode> STAR_OP() { return getTokens(CParser.STAR_OP); }
		public TerminalNode STAR_OP(int i) {
			return getToken(CParser.STAR_OP, i);
		}
		public TerminalNode LBRACKET() { return getToken(CParser.LBRACKET, 0); }
		public TerminalNode INT_LITERAL() { return getToken(CParser.INT_LITERAL, 0); }
		public TerminalNode RBRACKET() { return getToken(CParser.RBRACKET, 0); }
		public TerminalNode ASSIGN_OP() { return getToken(CParser.ASSIGN_OP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> CONST() { return getTokens(CParser.CONST); }
		public TerminalNode CONST(int i) {
			return getToken(CParser.CONST, i);
		}
		public DeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarator; }
	}

	public final DeclaratorContext declarator() throws RecognitionException {
		DeclaratorContext _localctx = new DeclaratorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_declarator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STAR_OP) {
				{
				{
				setState(238);
				match(STAR_OP);
				setState(240);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==CONST) {
					{
					setState(239);
					match(CONST);
					}
				}

				}
				}
				setState(246);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(247);
			match(IDENTIFIER);
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBRACKET) {
				{
				setState(248);
				match(LBRACKET);
				setState(249);
				match(INT_LITERAL);
				setState(250);
				match(RBRACKET);
				}
			}

			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN_OP) {
				{
				setState(253);
				match(ASSIGN_OP);
				setState(254);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(CParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(CParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CParser.COMMA, i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(IDENTIFIER);
			setState(258);
			match(LPAREN);
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 44)) & ~0x3f) == 0 && ((1L << (_la - 44)) & ((1L << (INCREMENT_OP - 44)) | (1L << (DECREMENT_OP - 44)) | (1L << (PLUS_OP - 44)) | (1L << (MINUS_OP - 44)) | (1L << (STAR_OP - 44)) | (1L << (AMPERSAND_OP - 44)) | (1L << (NOT_OP - 44)) | (1L << (LPAREN - 44)) | (1L << (INT_LITERAL - 44)) | (1L << (REAL_LITERAL - 44)) | (1L << (CHAR_LITERAL - 44)) | (1L << (STRING_LITERAL - 44)) | (1L << (IDENTIFIER - 44)))) != 0)) {
				{
				setState(259);
				expression(0);
				setState(264);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(260);
					match(COMMA);
					setState(261);
					expression(0);
					}
					}
					setState(266);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(269);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 5);
		case 6:
			return precpred(_ctx, 4);
		case 7:
			return precpred(_ctx, 14);
		case 8:
			return precpred(_ctx, 12);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3Y\u0112\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\2\5\2(\n\2\3\2\3\2\3\2\3\2\7\2.\n\2\f\2\16\2\61\13\2\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\7\39\n\3\f\3\16\3<\13\3\5\3>\n\3\3\3\3\3\3\4\3\4\3"+
		"\4\5\4E\n\4\5\4G\n\4\3\4\3\4\3\5\3\5\5\5M\n\5\3\5\5\5P\n\5\3\6\3\6\3\6"+
		"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7^\n\7\3\b\3\b\3\b\3\b\3\b\7\b"+
		"e\n\b\f\b\16\bh\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0080\n\t\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0093\n\n\3\n\3"+
		"\n\5\n\u0097\n\n\3\n\3\n\5\n\u009b\n\n\3\n\3\n\5\n\u009f\n\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\5\13\u00a7\n\13\3\13\5\13\u00aa\n\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b6\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\7\f\u00d4\n\f\f\f\16\f\u00d7\13\f\3\r\3\r\3\r\3\r\5\r\u00dd"+
		"\n\r\3\16\3\16\3\17\5\17\u00e2\n\17\3\17\3\17\5\17\u00e6\n\17\3\20\3\20"+
		"\3\20\3\20\7\20\u00ec\n\20\f\20\16\20\u00ef\13\20\3\21\3\21\5\21\u00f3"+
		"\n\21\7\21\u00f5\n\21\f\21\16\21\u00f8\13\21\3\21\3\21\3\21\3\21\5\21"+
		"\u00fe\n\21\3\21\3\21\5\21\u0102\n\21\3\22\3\22\3\22\3\22\3\22\7\22\u0109"+
		"\n\22\f\22\16\22\u010c\13\22\5\22\u010e\n\22\3\22\3\22\3\22\2\3\26\23"+
		"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\n\5\2\6\6\17\17\23\23\5\2"+
		".\62\66\66;;\3\2\62\64\3\2\60\61\3\2@C\3\2>?\3\2#-\3\2./\2\u0133\2/\3"+
		"\2\2\2\4\62\3\2\2\2\6A\3\2\2\2\bO\3\2\2\2\nQ\3\2\2\2\f]\3\2\2\2\16_\3"+
		"\2\2\2\20\177\3\2\2\2\22\u009e\3\2\2\2\24\u00a9\3\2\2\2\26\u00b5\3\2\2"+
		"\2\30\u00dc\3\2\2\2\32\u00de\3\2\2\2\34\u00e1\3\2\2\2\36\u00e7\3\2\2\2"+
		" \u00f6\3\2\2\2\"\u0103\3\2\2\2$\'\5\4\3\2%(\7N\2\2&(\5\16\b\2\'%\3\2"+
		"\2\2\'&\3\2\2\2(.\3\2\2\2)*\5\36\20\2*+\7N\2\2+.\3\2\2\2,.\5\n\6\2-$\3"+
		"\2\2\2-)\3\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\3\3\2"+
		"\2\2\61/\3\2\2\2\62\63\5\b\5\2\63\64\7T\2\2\64=\7G\2\2\65:\5\6\4\2\66"+
		"\67\7O\2\2\679\5\6\4\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2"+
		"\2\2<:\3\2\2\2=\65\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7H\2\2@\5\3\2\2\2AF\5"+
		"\34\17\2BD\7\62\2\2CE\7\7\2\2DC\3\2\2\2DE\3\2\2\2EG\3\2\2\2FB\3\2\2\2"+
		"FG\3\2\2\2GH\3\2\2\2HI\7T\2\2I\7\3\2\2\2JL\t\2\2\2KM\7\62\2\2LK\3\2\2"+
		"\2LM\3\2\2\2MP\3\2\2\2NP\7 \2\2OJ\3\2\2\2ON\3\2\2\2P\t\3\2\2\2QR\7U\2"+
		"\2RS\7@\2\2ST\7V\2\2TU\7B\2\2U\13\3\2\2\2V^\5\16\b\2WX\5\26\f\2XY\7N\2"+
		"\2Y^\3\2\2\2Z^\5\20\t\2[^\5\22\n\2\\^\5\24\13\2]V\3\2\2\2]W\3\2\2\2]Z"+
		"\3\2\2\2][\3\2\2\2]\\\3\2\2\2^\r\3\2\2\2_f\7K\2\2`e\5\f\7\2ab\5\36\20"+
		"\2bc\7N\2\2ce\3\2\2\2d`\3\2\2\2da\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2"+
		"\2gi\3\2\2\2hf\3\2\2\2ij\7L\2\2j\17\3\2\2\2kl\7\22\2\2lm\7G\2\2mn\5\26"+
		"\f\2no\7H\2\2op\5\f\7\2p\u0080\3\2\2\2qr\7\22\2\2rs\7G\2\2st\5\26\f\2"+
		"tu\7H\2\2uv\5\f\7\2vw\7\f\2\2wx\5\f\7\2x\u0080\3\2\2\2yz\7\34\2\2z{\7"+
		"G\2\2{|\5\26\f\2|}\7H\2\2}~\5\f\7\2~\u0080\3\2\2\2\177k\3\2\2\2\177q\3"+
		"\2\2\2\177y\3\2\2\2\u0080\21\3\2\2\2\u0081\u0082\7\"\2\2\u0082\u0083\7"+
		"G\2\2\u0083\u0084\5\26\f\2\u0084\u0085\7H\2\2\u0085\u0086\5\f\7\2\u0086"+
		"\u009f\3\2\2\2\u0087\u0088\7\n\2\2\u0088\u0089\5\f\7\2\u0089\u008a\7\""+
		"\2\2\u008a\u008b\7G\2\2\u008b\u008c\5\26\f\2\u008c\u008d\7H\2\2\u008d"+
		"\u008e\7N\2\2\u008e\u009f\3\2\2\2\u008f\u0090\7\20\2\2\u0090\u0092\7G"+
		"\2\2\u0091\u0093\5\36\20\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\u0096\7N\2\2\u0095\u0097\5\26\f\2\u0096\u0095\3\2"+
		"\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\7N\2\2\u0099"+
		"\u009b\5\26\f\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3"+
		"\2\2\2\u009c\u009d\7H\2\2\u009d\u009f\5\f\7\2\u009e\u0081\3\2\2\2\u009e"+
		"\u0087\3\2\2\2\u009e\u008f\3\2\2\2\u009f\23\3\2\2\2\u00a0\u00a1\7\4\2"+
		"\2\u00a1\u00aa\7N\2\2\u00a2\u00a3\7\b\2\2\u00a3\u00aa\7N\2\2\u00a4\u00a6"+
		"\7\26\2\2\u00a5\u00a7\5\26\f\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2"+
		"\u00a7\u00a8\3\2\2\2\u00a8\u00aa\7N\2\2\u00a9\u00a0\3\2\2\2\u00a9\u00a2"+
		"\3\2\2\2\u00a9\u00a4\3\2\2\2\u00aa\25\3\2\2\2\u00ab\u00ac\b\f\1\2\u00ac"+
		"\u00b6\5\"\22\2\u00ad\u00ae\t\3\2\2\u00ae\u00b6\5\26\f\r\u00af\u00b0\7"+
		"G\2\2\u00b0\u00b1\5\26\f\2\u00b1\u00b2\7H\2\2\u00b2\u00b6\3\2\2\2\u00b3"+
		"\u00b6\5\32\16\2\u00b4\u00b6\5\30\r\2\u00b5\u00ab\3\2\2\2\u00b5\u00ad"+
		"\3\2\2\2\u00b5\u00af\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6"+
		"\u00d5\3\2\2\2\u00b7\u00b8\f\f\2\2\u00b8\u00b9\t\4\2\2\u00b9\u00d4\5\26"+
		"\f\r\u00ba\u00bb\f\13\2\2\u00bb\u00bc\t\5\2\2\u00bc\u00d4\5\26\f\f\u00bd"+
		"\u00be\f\n\2\2\u00be\u00bf\t\6\2\2\u00bf\u00d4\5\26\f\13\u00c0\u00c1\f"+
		"\t\2\2\u00c1\u00c2\t\7\2\2\u00c2\u00d4\5\26\f\n\u00c3\u00c4\f\b\2\2\u00c4"+
		"\u00c5\7<\2\2\u00c5\u00d4\5\26\f\t\u00c6\u00c7\f\7\2\2\u00c7\u00c8\7="+
		"\2\2\u00c8\u00d4\5\26\f\b\u00c9\u00ca\f\6\2\2\u00ca\u00cb\t\b\2\2\u00cb"+
		"\u00d4\5\26\f\6\u00cc\u00cd\f\20\2\2\u00cd\u00d4\t\t\2\2\u00ce\u00cf\f"+
		"\16\2\2\u00cf\u00d0\7I\2\2\u00d0\u00d1\5\26\f\2\u00d1\u00d2\7J\2\2\u00d2"+
		"\u00d4\3\2\2\2\u00d3\u00b7\3\2\2\2\u00d3\u00ba\3\2\2\2\u00d3\u00bd\3\2"+
		"\2\2\u00d3\u00c0\3\2\2\2\u00d3\u00c3\3\2\2\2\u00d3\u00c6\3\2\2\2\u00d3"+
		"\u00c9\3\2\2\2\u00d3\u00cc\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d4\u00d7\3\2"+
		"\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\27\3\2\2\2\u00d7\u00d5"+
		"\3\2\2\2\u00d8\u00dd\7R\2\2\u00d9\u00dd\7S\2\2\u00da\u00dd\7P\2\2\u00db"+
		"\u00dd\7Q\2\2\u00dc\u00d8\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2"+
		"\2\2\u00dc\u00db\3\2\2\2\u00dd\31\3\2\2\2\u00de\u00df\7T\2\2\u00df\33"+
		"\3\2\2\2\u00e0\u00e2\7\7\2\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2"+
		"\u00e3\3\2\2\2\u00e3\u00e5\t\2\2\2\u00e4\u00e6\7\7\2\2\u00e5\u00e4\3\2"+
		"\2\2\u00e5\u00e6\3\2\2\2\u00e6\35\3\2\2\2\u00e7\u00e8\5\34\17\2\u00e8"+
		"\u00ed\5 \21\2\u00e9\u00ea\7O\2\2\u00ea\u00ec\5 \21\2\u00eb\u00e9\3\2"+
		"\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee"+
		"\37\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f2\7\62\2\2\u00f1\u00f3\7\7\2"+
		"\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f0"+
		"\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7"+
		"\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fd\7T\2\2\u00fa\u00fb\7I\2"+
		"\2\u00fb\u00fc\7P\2\2\u00fc\u00fe\7J\2\2\u00fd\u00fa\3\2\2\2\u00fd\u00fe"+
		"\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u0100\7#\2\2\u0100\u0102\5\26\f\2\u0101"+
		"\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102!\3\2\2\2\u0103\u0104\7T\2\2\u0104"+
		"\u010d\7G\2\2\u0105\u010a\5\26\f\2\u0106\u0107\7O\2\2\u0107\u0109\5\26"+
		"\f\2\u0108\u0106\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a"+
		"\u010b\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0105\3\2"+
		"\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7H\2\2\u0110"+
		"#\3\2\2\2\"\'-/:=DFLO]df\177\u0092\u0096\u009a\u009e\u00a6\u00a9\u00b5"+
		"\u00d3\u00d5\u00dc\u00e1\u00e5\u00ed\u00f2\u00f6\u00fd\u0101\u010a\u010d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}