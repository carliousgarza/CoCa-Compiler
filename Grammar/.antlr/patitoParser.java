// Generated from /Users/amionej/Documents/Tec/8semestre/compis/CoCa-Compiler/Grammar/patito.g4 by ANTLR 4.7.1

  from Compiler.compiler import *
  from Compiler.function import *
  from Compiler.variable import *
  from Compiler.interpreter import *
  interpreter = Interpreter()
  compiler = Compiler()

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class patitoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT=1, LINE_COMMENT=2, WS=3, LESS=4, GREATER=5, LESS_EQUAL=6, GREATER_EQUAL=7, 
		EQUAL=8, NOT_EQUAL=9, ASSIGN=10, AND=11, OR=12, ADD=13, SUB=14, MULT=15, 
		DIV=16, LEFT_PARENTHESIS=17, RIGHT_PARENTHESIS=18, LEFT_BRACKET=19, RIGHT_BRACKET=20, 
		LEFT_CURLY=21, RIGHT_CURLY=22, DETERMINANT=23, TRANSPOSE=24, INVERSE=25, 
		COMMA=26, COLON=27, SEMICOLON=28, PROGRAM=29, MAIN=30, FUNCTION=31, RETURN=32, 
		INPUT=33, PRINT=34, IF=35, THEN=36, ELSE=37, WHILE=38, DO=39, FROM=40, 
		TO=41, VAR=42, BOOL=43, INT=44, FLOAT=45, STRING=46, CHAR=47, CTE_BOOL=48, 
		CTE_FLOAT=49, CTE_INT=50, CTE_CHAR=51, CTE_STRING=52, VOID=53, ID=54;
	public static final int
		RULE_program = 0, RULE_declarevars = 1, RULE_variables = 2, RULE_vartypes = 3, 
		RULE_constant = 4, RULE_varindividual = 5, RULE_functions = 6, RULE_function = 7, 
		RULE_functiontype = 8, RULE_parameters = 9, RULE_hexp = 10, RULE_mexp = 11, 
		RULE_sexp = 12, RULE_exp = 13, RULE_term = 14, RULE_factor = 15, RULE_statute = 16, 
		RULE_assignation = 17, RULE_voidcall = 18, RULE_returncall = 19, RULE_indexvariable = 20, 
		RULE_read = 21, RULE_write = 22, RULE_conditional = 23, RULE_whileloop = 24, 
		RULE_fromloop = 25, RULE_mainfunc = 26;
	public static final String[] ruleNames = {
		"program", "declarevars", "variables", "vartypes", "constant", "varindividual", 
		"functions", "function", "functiontype", "parameters", "hexp", "mexp", 
		"sexp", "exp", "term", "factor", "statute", "assignation", "voidcall", 
		"returncall", "indexvariable", "read", "write", "conditional", "whileloop", 
		"fromloop", "mainfunc"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
		"'='", "'&&'", "'||'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'['", 
		"']'", "'{'", "'}'", "'$'", "'\u00A1'", "'?'", "','", "':'", "';'", "'program'", 
		"'main'", "'function'", "'return'", "'input'", "'print'", "'if'", "'then'", 
		"'else'", "'while'", "'do'", "'from'", "'to'", "'var'", "'bool'", "'int'", 
		"'float'", "'string'", "'char'", null, null, null, null, null, "'void'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "COMMENT", "LINE_COMMENT", "WS", "LESS", "GREATER", "LESS_EQUAL", 
		"GREATER_EQUAL", "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", "OR", "ADD", "SUB", 
		"MULT", "DIV", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
		"RIGHT_BRACKET", "LEFT_CURLY", "RIGHT_CURLY", "DETERMINANT", "TRANSPOSE", 
		"INVERSE", "COMMA", "COLON", "SEMICOLON", "PROGRAM", "MAIN", "FUNCTION", 
		"RETURN", "INPUT", "PRINT", "IF", "THEN", "ELSE", "WHILE", "DO", "FROM", 
		"TO", "VAR", "BOOL", "INT", "FLOAT", "STRING", "CHAR", "CTE_BOOL", "CTE_FLOAT", 
		"CTE_INT", "CTE_CHAR", "CTE_STRING", "VOID", "ID"
	};
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
	public String getGrammarFileName() { return "patito.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public patitoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(patitoParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public DeclarevarsContext declarevars() {
			return getRuleContext(DeclarevarsContext.class,0);
		}
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public MainfuncContext mainfunc() {
			return getRuleContext(MainfuncContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(PROGRAM);
			setState(55);
			match(ID);
			setState(56);
			match(SEMICOLON);
			setState(57);
			declarevars();
			setState(58);
			functions();
			setState(59);
			mainfunc();
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

	public static class DeclarevarsContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(patitoParser.VAR, 0); }
		public List<VariablesContext> variables() {
			return getRuleContexts(VariablesContext.class);
		}
		public VariablesContext variables(int i) {
			return getRuleContext(VariablesContext.class,i);
		}
		public DeclarevarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarevars; }
	}

	public final DeclarevarsContext declarevars() throws RecognitionException {
		DeclarevarsContext _localctx = new DeclarevarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declarevars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(VAR);
			setState(63); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(62);
				variables();
				}
				}
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << CHAR))) != 0) );
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

	public static class VariablesContext extends ParserRuleContext {
		public VartypesContext vartypes() {
			return getRuleContext(VartypesContext.class,0);
		}
		public TerminalNode COLON() { return getToken(patitoParser.COLON, 0); }
		public List<VarindividualContext> varindividual() {
			return getRuleContexts(VarindividualContext.class);
		}
		public VarindividualContext varindividual(int i) {
			return getRuleContext(VarindividualContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public VariablesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variables; }
	}

	public final VariablesContext variables() throws RecognitionException {
		VariablesContext _localctx = new VariablesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variables);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			vartypes();
			setState(68);
			match(COLON);
			setState(69);
			varindividual();
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(70);
				match(COMMA);
				setState(71);
				varindividual();
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(77);
			match(SEMICOLON);
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

	public static class VartypesContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(patitoParser.INT, 0); }
		public TerminalNode BOOL() { return getToken(patitoParser.BOOL, 0); }
		public TerminalNode FLOAT() { return getToken(patitoParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(patitoParser.STRING, 0); }
		public TerminalNode CHAR() { return getToken(patitoParser.CHAR, 0); }
		public VartypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vartypes; }
	}

	public final VartypesContext vartypes() throws RecognitionException {
		VartypesContext _localctx = new VartypesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vartypes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << CHAR))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode CTE_BOOL() { return getToken(patitoParser.CTE_BOOL, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(patitoParser.CTE_FLOAT, 0); }
		public TerminalNode CTE_INT() { return getToken(patitoParser.CTE_INT, 0); }
		public TerminalNode CTE_CHAR() { return getToken(patitoParser.CTE_CHAR, 0); }
		public TerminalNode CTE_STRING() { return getToken(patitoParser.CTE_STRING, 0); }
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_constant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CTE_BOOL) | (1L << CTE_FLOAT) | (1L << CTE_INT) | (1L << CTE_CHAR) | (1L << CTE_STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class VarindividualContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(patitoParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(patitoParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> CTE_INT() { return getTokens(patitoParser.CTE_INT); }
		public TerminalNode CTE_INT(int i) {
			return getToken(patitoParser.CTE_INT, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(patitoParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(patitoParser.RIGHT_BRACKET, i);
		}
		public VarindividualContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varindividual; }
	}

	public final VarindividualContext varindividual() throws RecognitionException {
		VarindividualContext _localctx = new VarindividualContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varindividual);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(ID);
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(84);
				match(LEFT_BRACKET);
				setState(85);
				match(CTE_INT);
				setState(86);
				match(RIGHT_BRACKET);
				}
				break;
			case 2:
				{
				setState(87);
				match(LEFT_BRACKET);
				setState(88);
				match(CTE_INT);
				setState(89);
				match(RIGHT_BRACKET);
				setState(90);
				match(LEFT_BRACKET);
				setState(91);
				match(CTE_INT);
				setState(92);
				match(RIGHT_BRACKET);
				}
				break;
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

	public static class FunctionsContext extends ParserRuleContext {
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public FunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functions; }
	}

	public final FunctionsContext functions() throws RecognitionException {
		FunctionsContext _localctx = new FunctionsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(95);
				function();
				}
				}
				setState(98); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==FUNCTION );
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

	public static class FunctionContext extends ParserRuleContext {
		public FunctiontypeContext functiontype;
		public Token ID;
		public TerminalNode FUNCTION() { return getToken(patitoParser.FUNCTION, 0); }
		public FunctiontypeContext functiontype() {
			return getRuleContext(FunctiontypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode LEFT_CURLY() { return getToken(patitoParser.LEFT_CURLY, 0); }
		public TerminalNode RIGHT_CURLY() { return getToken(patitoParser.RIGHT_CURLY, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public DeclarevarsContext declarevars() {
			return getRuleContext(DeclarevarsContext.class,0);
		}
		public StatuteContext statute() {
			return getRuleContext(StatuteContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(FUNCTION);
			setState(101);
			((FunctionContext)_localctx).functiontype = functiontype();
			setState(102);
			((FunctionContext)_localctx).ID = match(ID);
			compiler.currentFunction=Function((((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null), (((FunctionContext)_localctx).functiontype!=null?_input.getText(((FunctionContext)_localctx).functiontype.start,((FunctionContext)_localctx).functiontype.stop):null), {}, {})
			setState(104);
			match(LEFT_PARENTHESIS);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << CHAR))) != 0)) {
				{
				setState(105);
				parameters();
				}
			}

			setState(108);
			match(RIGHT_PARENTHESIS);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(109);
				declarevars();
				}
			}

			setState(112);
			match(LEFT_CURLY);
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(113);
				statute();
				}
				break;
			}
			setState(116);
			match(RIGHT_CURLY);
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

	public static class FunctiontypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(patitoParser.INT, 0); }
		public TerminalNode BOOL() { return getToken(patitoParser.BOOL, 0); }
		public TerminalNode FLOAT() { return getToken(patitoParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(patitoParser.STRING, 0); }
		public TerminalNode CHAR() { return getToken(patitoParser.CHAR, 0); }
		public TerminalNode VOID() { return getToken(patitoParser.VOID, 0); }
		public FunctiontypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functiontype; }
	}

	public final FunctiontypeContext functiontype() throws RecognitionException {
		FunctiontypeContext _localctx = new FunctiontypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_functiontype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << CHAR) | (1L << VOID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class ParametersContext extends ParserRuleContext {
		public VartypesContext vartypes;
		public Token ID;
		public List<VartypesContext> vartypes() {
			return getRuleContexts(VartypesContext.class);
		}
		public VartypesContext vartypes(int i) {
			return getRuleContext(VartypesContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(patitoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(patitoParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			((ParametersContext)_localctx).vartypes = vartypes();
			setState(121);
			((ParametersContext)_localctx).ID = match(ID);
			compiler.currentFunction._update_parameters((((ParametersContext)_localctx).vartypes!=null?_input.getText(((ParametersContext)_localctx).vartypes.start,((ParametersContext)_localctx).vartypes.stop):null), (((ParametersContext)_localctx).ID!=null?((ParametersContext)_localctx).ID.getText():null))
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(123);
				match(COMMA);
				setState(124);
				((ParametersContext)_localctx).vartypes = vartypes();
				setState(125);
				((ParametersContext)_localctx).ID = match(ID);
				compiler.currentFunction._update_parameters((((ParametersContext)_localctx).vartypes!=null?_input.getText(((ParametersContext)_localctx).vartypes.start,((ParametersContext)_localctx).vartypes.stop):null), (((ParametersContext)_localctx).ID!=null?((ParametersContext)_localctx).ID.getText():null))
				}
				}
				setState(132);
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

	public static class HexpContext extends ParserRuleContext {
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(patitoParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(patitoParser.ASSIGN, i);
		}
		public HexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hexp; }
	}

	public final HexpContext hexp() throws RecognitionException {
		HexpContext _localctx = new HexpContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_hexp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			mexp();
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ASSIGN) {
				{
				{
				setState(134);
				match(ASSIGN);
				setState(135);
				mexp();
				}
				}
				setState(140);
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

	public static class MexpContext extends ParserRuleContext {
		public Token AND;
		public Token OR;
		public List<SexpContext> sexp() {
			return getRuleContexts(SexpContext.class);
		}
		public SexpContext sexp(int i) {
			return getRuleContext(SexpContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(patitoParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(patitoParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(patitoParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(patitoParser.OR, i);
		}
		public MexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mexp; }
	}

	public final MexpContext mexp() throws RecognitionException {
		MexpContext _localctx = new MexpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_mexp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			sexp();
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(146);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(142);
					((MexpContext)_localctx).AND = match(AND);
					interpreter.addOperator((((MexpContext)_localctx).AND!=null?((MexpContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(144);
					((MexpContext)_localctx).OR = match(OR);
					interpreter.addOperator((((MexpContext)_localctx).OR!=null?((MexpContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(148);
				sexp();
				}
				}
				setState(153);
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

	public static class SexpContext extends ParserRuleContext {
		public Token GREATER;
		public Token LESS;
		public Token GREATER_EQUAL;
		public Token LESS_EQUAL;
		public Token NOT_EQUAL;
		public Token EQUAL;
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode GREATER() { return getToken(patitoParser.GREATER, 0); }
		public TerminalNode LESS() { return getToken(patitoParser.LESS, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(patitoParser.GREATER_EQUAL, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(patitoParser.LESS_EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(patitoParser.NOT_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(patitoParser.EQUAL, 0); }
		public SexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sexp; }
	}

	public final SexpContext sexp() throws RecognitionException {
		SexpContext _localctx = new SexpContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sexp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			exp();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LESS_EQUAL) | (1L << GREATER_EQUAL) | (1L << EQUAL) | (1L << NOT_EQUAL))) != 0)) {
				{
				setState(167);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GREATER:
					{
					setState(155);
					((SexpContext)_localctx).GREATER = match(GREATER);
					interpreter.addOperator((((SexpContext)_localctx).GREATER!=null?((SexpContext)_localctx).GREATER.getText():null))
					}
					break;
				case LESS:
					{
					setState(157);
					((SexpContext)_localctx).LESS = match(LESS);
					interpreter.addOperator((((SexpContext)_localctx).LESS!=null?((SexpContext)_localctx).LESS.getText():null))
					}
					break;
				case GREATER_EQUAL:
					{
					setState(159);
					((SexpContext)_localctx).GREATER_EQUAL = match(GREATER_EQUAL);
					interpreter.addOperator((((SexpContext)_localctx).GREATER_EQUAL!=null?((SexpContext)_localctx).GREATER_EQUAL.getText():null))
					}
					break;
				case LESS_EQUAL:
					{
					setState(161);
					((SexpContext)_localctx).LESS_EQUAL = match(LESS_EQUAL);
					interpreter.addOperator((((SexpContext)_localctx).LESS_EQUAL!=null?((SexpContext)_localctx).LESS_EQUAL.getText():null))
					}
					break;
				case NOT_EQUAL:
					{
					setState(163);
					((SexpContext)_localctx).NOT_EQUAL = match(NOT_EQUAL);
					interpreter.addOperator((((SexpContext)_localctx).NOT_EQUAL!=null?((SexpContext)_localctx).NOT_EQUAL.getText():null))
					}
					break;
				case EQUAL:
					{
					setState(165);
					((SexpContext)_localctx).EQUAL = match(EQUAL);
					interpreter.addOperator((((SexpContext)_localctx).EQUAL!=null?((SexpContext)_localctx).EQUAL.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(169);
				exp();
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

	public static class ExpContext extends ParserRuleContext {
		public Token ADD;
		public Token SUB;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> ADD() { return getTokens(patitoParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(patitoParser.ADD, i);
		}
		public List<TerminalNode> SUB() { return getTokens(patitoParser.SUB); }
		public TerminalNode SUB(int i) {
			return getToken(patitoParser.SUB, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			term();
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADD || _la==SUB) {
				{
				{
				setState(177);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ADD:
					{
					setState(173);
					((ExpContext)_localctx).ADD = match(ADD);
					interpreter.addOperator((((ExpContext)_localctx).ADD!=null?((ExpContext)_localctx).ADD.getText():null))
					}
					break;
				case SUB:
					{
					setState(175);
					((ExpContext)_localctx).SUB = match(SUB);
					interpreter.addOperator((((ExpContext)_localctx).SUB!=null?((ExpContext)_localctx).SUB.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(179);
				term();
				}
				}
				setState(184);
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

	public static class TermContext extends ParserRuleContext {
		public Token MULT;
		public Token DIV;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(patitoParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(patitoParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(patitoParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(patitoParser.DIV, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			factor();
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(190);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULT:
					{
					setState(186);
					((TermContext)_localctx).MULT = match(MULT);
					interpreter.addOperator((((TermContext)_localctx).MULT!=null?((TermContext)_localctx).MULT.getText():null))
					}
					break;
				case DIV:
					{
					setState(188);
					((TermContext)_localctx).DIV = match(DIV);
					interpreter.addOperator((((TermContext)_localctx).DIV!=null?((TermContext)_localctx).DIV.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(192);
				factor();
				}
				}
				setState(197);
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

	public static class FactorContext extends ParserRuleContext {
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public List<HexpContext> hexp() {
			return getRuleContexts(HexpContext.class);
		}
		public HexpContext hexp(int i) {
			return getRuleContext(HexpContext.class,i);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(patitoParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(patitoParser.LEFT_BRACKET, i);
		}
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(patitoParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(patitoParser.RIGHT_BRACKET, i);
		}
		public TerminalNode DETERMINANT() { return getToken(patitoParser.DETERMINANT, 0); }
		public TerminalNode TRANSPOSE() { return getToken(patitoParser.TRANSPOSE, 0); }
		public TerminalNode INVERSE() { return getToken(patitoParser.INVERSE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_BOOL:
			case CTE_FLOAT:
			case CTE_INT:
			case CTE_CHAR:
			case CTE_STRING:
				{
				setState(198);
				constant();
				}
				break;
			case LEFT_PARENTHESIS:
				{
				setState(199);
				match(LEFT_PARENTHESIS);
				interpreter.addParenthesis()
				setState(201);
				hexp();
				setState(202);
				match(RIGHT_PARENTHESIS);
				interpreter.popParenthesis()
				}
				break;
			case ID:
				{
				setState(205);
				match(ID);
				setState(234);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
				case 1:
					{
					}
					break;
				case 2:
					{
					setState(207);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DETERMINANT) | (1L << TRANSPOSE) | (1L << INVERSE))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					break;
				case 3:
					{
					setState(208);
					match(LEFT_BRACKET);
					setState(209);
					mexp();
					setState(210);
					match(RIGHT_BRACKET);
					}
					break;
				case 4:
					{
					setState(212);
					match(LEFT_BRACKET);
					setState(213);
					mexp();
					setState(214);
					match(RIGHT_BRACKET);
					setState(215);
					match(LEFT_BRACKET);
					setState(216);
					mexp();
					setState(217);
					match(RIGHT_BRACKET);
					}
					break;
				case 5:
					{
					setState(219);
					match(LEFT_PARENTHESIS);
					interpreter.addParenthesis()
					setState(230);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case RIGHT_PARENTHESIS:
						{
						}
						break;
					case LEFT_PARENTHESIS:
					case CTE_BOOL:
					case CTE_FLOAT:
					case CTE_INT:
					case CTE_CHAR:
					case CTE_STRING:
					case ID:
						{
						setState(222);
						hexp();
						setState(227);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(223);
							match(COMMA);
							setState(224);
							hexp();
							}
							}
							setState(229);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(232);
					match(RIGHT_PARENTHESIS);
					interpreter.popParenthesis()
					}
					break;
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class StatuteContext extends ParserRuleContext {
		public List<AssignationContext> assignation() {
			return getRuleContexts(AssignationContext.class);
		}
		public AssignationContext assignation(int i) {
			return getRuleContext(AssignationContext.class,i);
		}
		public List<VoidcallContext> voidcall() {
			return getRuleContexts(VoidcallContext.class);
		}
		public VoidcallContext voidcall(int i) {
			return getRuleContext(VoidcallContext.class,i);
		}
		public List<ReturncallContext> returncall() {
			return getRuleContexts(ReturncallContext.class);
		}
		public ReturncallContext returncall(int i) {
			return getRuleContext(ReturncallContext.class,i);
		}
		public List<ReadContext> read() {
			return getRuleContexts(ReadContext.class);
		}
		public ReadContext read(int i) {
			return getRuleContext(ReadContext.class,i);
		}
		public List<WriteContext> write() {
			return getRuleContexts(WriteContext.class);
		}
		public WriteContext write(int i) {
			return getRuleContext(WriteContext.class,i);
		}
		public List<ConditionalContext> conditional() {
			return getRuleContexts(ConditionalContext.class);
		}
		public ConditionalContext conditional(int i) {
			return getRuleContext(ConditionalContext.class,i);
		}
		public List<WhileloopContext> whileloop() {
			return getRuleContexts(WhileloopContext.class);
		}
		public WhileloopContext whileloop(int i) {
			return getRuleContext(WhileloopContext.class,i);
		}
		public List<FromloopContext> fromloop() {
			return getRuleContexts(FromloopContext.class);
		}
		public FromloopContext fromloop(int i) {
			return getRuleContext(FromloopContext.class,i);
		}
		public StatuteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statute; }
	}

	public final StatuteContext statute() throws RecognitionException {
		StatuteContext _localctx = new StatuteContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_statute);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << INPUT) | (1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << FROM) | (1L << ID))) != 0)) {
				{
				setState(246);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(238);
					assignation();
					}
					break;
				case 2:
					{
					setState(239);
					voidcall();
					}
					break;
				case 3:
					{
					setState(240);
					returncall();
					}
					break;
				case 4:
					{
					setState(241);
					read();
					}
					break;
				case 5:
					{
					setState(242);
					write();
					}
					break;
				case 6:
					{
					setState(243);
					conditional();
					}
					break;
				case 7:
					{
					setState(244);
					whileloop();
					}
					break;
				case 8:
					{
					setState(245);
					fromloop();
					}
					break;
				}
				}
				setState(250);
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

	public static class AssignationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(patitoParser.ASSIGN, 0); }
		public HexpContext hexp() {
			return getRuleContext(HexpContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(patitoParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(patitoParser.LEFT_BRACKET, i);
		}
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(patitoParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(patitoParser.RIGHT_BRACKET, i);
		}
		public AssignationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignation; }
	}

	public final AssignationContext assignation() throws RecognitionException {
		AssignationContext _localctx = new AssignationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_assignation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(ID);
			setState(264);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				}
				break;
			case 2:
				{
				setState(253);
				match(LEFT_BRACKET);
				setState(254);
				mexp();
				setState(255);
				match(RIGHT_BRACKET);
				}
				break;
			case 3:
				{
				setState(257);
				match(LEFT_BRACKET);
				setState(258);
				mexp();
				setState(259);
				match(RIGHT_BRACKET);
				setState(260);
				match(LEFT_BRACKET);
				setState(261);
				mexp();
				setState(262);
				match(RIGHT_BRACKET);
				}
				break;
			}
			setState(266);
			match(ASSIGN);
			setState(267);
			hexp();
			setState(268);
			match(SEMICOLON);
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

	public static class VoidcallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public VoidcallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_voidcall; }
	}

	public final VoidcallContext voidcall() throws RecognitionException {
		VoidcallContext _localctx = new VoidcallContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_voidcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(ID);
			setState(271);
			match(LEFT_PARENTHESIS);
			setState(281);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RIGHT_PARENTHESIS:
				{
				}
				break;
			case LEFT_PARENTHESIS:
			case CTE_BOOL:
			case CTE_FLOAT:
			case CTE_INT:
			case CTE_CHAR:
			case CTE_STRING:
			case ID:
				{
				setState(273);
				mexp();
				setState(278);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(274);
					match(COMMA);
					setState(275);
					mexp();
					}
					}
					setState(280);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(283);
			match(RIGHT_PARENTHESIS);
			setState(284);
			match(SEMICOLON);
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

	public static class ReturncallContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(patitoParser.RETURN, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public HexpContext hexp() {
			return getRuleContext(HexpContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public ReturncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returncall; }
	}

	public final ReturncallContext returncall() throws RecognitionException {
		ReturncallContext _localctx = new ReturncallContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_returncall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(RETURN);
			setState(287);
			match(LEFT_PARENTHESIS);
			setState(288);
			hexp();
			setState(289);
			match(RIGHT_PARENTHESIS);
			setState(290);
			match(SEMICOLON);
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

	public static class IndexvariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(patitoParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(patitoParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(patitoParser.LEFT_BRACKET, i);
		}
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(patitoParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(patitoParser.RIGHT_BRACKET, i);
		}
		public IndexvariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_indexvariable; }
	}

	public final IndexvariableContext indexvariable() throws RecognitionException {
		IndexvariableContext _localctx = new IndexvariableContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_indexvariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(ID);
			setState(305);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				{
				}
				break;
			case 2:
				{
				setState(294);
				match(LEFT_BRACKET);
				setState(295);
				mexp();
				setState(296);
				match(RIGHT_BRACKET);
				}
				break;
			case 3:
				{
				setState(298);
				match(LEFT_BRACKET);
				setState(299);
				mexp();
				setState(300);
				match(RIGHT_BRACKET);
				setState(301);
				match(LEFT_BRACKET);
				setState(302);
				mexp();
				setState(303);
				match(RIGHT_BRACKET);
				}
				break;
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

	public static class ReadContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(patitoParser.INPUT, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public List<IndexvariableContext> indexvariable() {
			return getRuleContexts(IndexvariableContext.class);
		}
		public IndexvariableContext indexvariable(int i) {
			return getRuleContext(IndexvariableContext.class,i);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_read);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(INPUT);
			setState(308);
			match(LEFT_PARENTHESIS);
			setState(309);
			indexvariable();
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(310);
				match(COMMA);
				setState(311);
				indexvariable();
				}
				}
				setState(316);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(317);
			match(RIGHT_PARENTHESIS);
			setState(318);
			match(SEMICOLON);
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

	public static class WriteContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(patitoParser.PRINT, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(patitoParser.SEMICOLON, 0); }
		public List<HexpContext> hexp() {
			return getRuleContexts(HexpContext.class);
		}
		public HexpContext hexp(int i) {
			return getRuleContext(HexpContext.class,i);
		}
		public List<TerminalNode> CTE_STRING() { return getTokens(patitoParser.CTE_STRING); }
		public TerminalNode CTE_STRING(int i) {
			return getToken(patitoParser.CTE_STRING, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(patitoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(patitoParser.COMMA, i);
		}
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_write);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			match(PRINT);
			setState(321);
			match(LEFT_PARENTHESIS);
			setState(324);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(322);
				hexp();
				}
				break;
			case 2:
				{
				setState(323);
				match(CTE_STRING);
				}
				break;
			}
			setState(333);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(326);
				match(COMMA);
				setState(329);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
				case 1:
					{
					setState(327);
					hexp();
					}
					break;
				case 2:
					{
					setState(328);
					match(CTE_STRING);
					}
					break;
				}
				}
				}
				setState(335);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(336);
			match(RIGHT_PARENTHESIS);
			setState(337);
			match(SEMICOLON);
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

	public static class ConditionalContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(patitoParser.IF, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public MexpContext mexp() {
			return getRuleContext(MexpContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode THEN() { return getToken(patitoParser.THEN, 0); }
		public List<TerminalNode> LEFT_CURLY() { return getTokens(patitoParser.LEFT_CURLY); }
		public TerminalNode LEFT_CURLY(int i) {
			return getToken(patitoParser.LEFT_CURLY, i);
		}
		public List<StatuteContext> statute() {
			return getRuleContexts(StatuteContext.class);
		}
		public StatuteContext statute(int i) {
			return getRuleContext(StatuteContext.class,i);
		}
		public List<TerminalNode> RIGHT_CURLY() { return getTokens(patitoParser.RIGHT_CURLY); }
		public TerminalNode RIGHT_CURLY(int i) {
			return getToken(patitoParser.RIGHT_CURLY, i);
		}
		public TerminalNode ELSE() { return getToken(patitoParser.ELSE, 0); }
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_conditional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(339);
			match(IF);
			setState(340);
			match(LEFT_PARENTHESIS);
			setState(341);
			mexp();
			setState(342);
			match(RIGHT_PARENTHESIS);
			setState(343);
			match(THEN);
			setState(344);
			match(LEFT_CURLY);
			setState(345);
			statute();
			setState(346);
			match(RIGHT_CURLY);
			setState(352);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(347);
				match(ELSE);
				setState(348);
				match(LEFT_CURLY);
				setState(349);
				statute();
				setState(350);
				match(RIGHT_CURLY);
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

	public static class WhileloopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(patitoParser.WHILE, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public MexpContext mexp() {
			return getRuleContext(MexpContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode DO() { return getToken(patitoParser.DO, 0); }
		public TerminalNode LEFT_CURLY() { return getToken(patitoParser.LEFT_CURLY, 0); }
		public StatuteContext statute() {
			return getRuleContext(StatuteContext.class,0);
		}
		public TerminalNode RIGHT_CURLY() { return getToken(patitoParser.RIGHT_CURLY, 0); }
		public WhileloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileloop; }
	}

	public final WhileloopContext whileloop() throws RecognitionException {
		WhileloopContext _localctx = new WhileloopContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_whileloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			match(WHILE);
			setState(355);
			match(LEFT_PARENTHESIS);
			setState(356);
			mexp();
			setState(357);
			match(RIGHT_PARENTHESIS);
			setState(358);
			match(DO);
			setState(359);
			match(LEFT_CURLY);
			setState(360);
			statute();
			setState(361);
			match(RIGHT_CURLY);
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

	public static class FromloopContext extends ParserRuleContext {
		public TerminalNode FROM() { return getToken(patitoParser.FROM, 0); }
		public IndexvariableContext indexvariable() {
			return getRuleContext(IndexvariableContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(patitoParser.ASSIGN, 0); }
		public List<MexpContext> mexp() {
			return getRuleContexts(MexpContext.class);
		}
		public MexpContext mexp(int i) {
			return getRuleContext(MexpContext.class,i);
		}
		public TerminalNode TO() { return getToken(patitoParser.TO, 0); }
		public TerminalNode DO() { return getToken(patitoParser.DO, 0); }
		public TerminalNode LEFT_CURLY() { return getToken(patitoParser.LEFT_CURLY, 0); }
		public StatuteContext statute() {
			return getRuleContext(StatuteContext.class,0);
		}
		public TerminalNode RIGHT_CURLY() { return getToken(patitoParser.RIGHT_CURLY, 0); }
		public FromloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fromloop; }
	}

	public final FromloopContext fromloop() throws RecognitionException {
		FromloopContext _localctx = new FromloopContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_fromloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(363);
			match(FROM);
			setState(364);
			indexvariable();
			setState(365);
			match(ASSIGN);
			setState(366);
			mexp();
			setState(367);
			match(TO);
			setState(368);
			mexp();
			setState(369);
			match(DO);
			setState(370);
			match(LEFT_CURLY);
			setState(371);
			statute();
			setState(372);
			match(RIGHT_CURLY);
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

	public static class MainfuncContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(patitoParser.MAIN, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(patitoParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(patitoParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode LEFT_CURLY() { return getToken(patitoParser.LEFT_CURLY, 0); }
		public StatuteContext statute() {
			return getRuleContext(StatuteContext.class,0);
		}
		public TerminalNode RIGHT_CURLY() { return getToken(patitoParser.RIGHT_CURLY, 0); }
		public MainfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainfunc; }
	}

	public final MainfuncContext mainfunc() throws RecognitionException {
		MainfuncContext _localctx = new MainfuncContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_mainfunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			match(MAIN);
			setState(375);
			match(LEFT_PARENTHESIS);
			setState(376);
			match(RIGHT_PARENTHESIS);
			setState(377);
			match(LEFT_CURLY);
			setState(378);
			statute();
			setState(379);
			match(RIGHT_CURLY);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38\u0180\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3"+
		"B\n\3\r\3\16\3C\3\4\3\4\3\4\3\4\3\4\7\4K\n\4\f\4\16\4N\13\4\3\4\3\4\3"+
		"\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7`\n\7\3\b\6"+
		"\bc\n\b\r\b\16\bd\3\t\3\t\3\t\3\t\3\t\3\t\5\tm\n\t\3\t\3\t\5\tq\n\t\3"+
		"\t\3\t\5\tu\n\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\7\13\u0083\n\13\f\13\16\13\u0086\13\13\3\f\3\f\3\f\7\f\u008b\n\f\f\f"+
		"\16\f\u008e\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u0095\n\r\3\r\7\r\u0098\n\r\f"+
		"\r\16\r\u009b\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\5\16\u00aa\n\16\3\16\5\16\u00ad\n\16\3\17\3\17\3\17\3\17"+
		"\3\17\5\17\u00b4\n\17\3\17\7\17\u00b7\n\17\f\17\16\17\u00ba\13\17\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00c1\n\20\3\20\7\20\u00c4\n\20\f\20\16\20\u00c7"+
		"\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\7\21\u00e4\n\21\f\21\16\21\u00e7\13\21\5\21\u00e9\n\21\3\21\3\21\5\21"+
		"\u00ed\n\21\5\21\u00ef\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7"+
		"\22\u00f9\n\22\f\22\16\22\u00fc\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u010b\n\23\3\23\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0117\n\24\f\24\16\24\u011a\13\24"+
		"\5\24\u011c\n\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0134\n\26"+
		"\3\27\3\27\3\27\3\27\3\27\7\27\u013b\n\27\f\27\16\27\u013e\13\27\3\27"+
		"\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0147\n\30\3\30\3\30\3\30\5\30\u014c"+
		"\n\30\7\30\u014e\n\30\f\30\16\30\u0151\13\30\3\30\3\30\3\30\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0163\n\31"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2"+
		"\6\3\2-\61\3\2\62\66\4\2-\61\67\67\3\2\31\33\2\u0195\28\3\2\2\2\4?\3\2"+
		"\2\2\6E\3\2\2\2\bQ\3\2\2\2\nS\3\2\2\2\fU\3\2\2\2\16b\3\2\2\2\20f\3\2\2"+
		"\2\22x\3\2\2\2\24z\3\2\2\2\26\u0087\3\2\2\2\30\u008f\3\2\2\2\32\u009c"+
		"\3\2\2\2\34\u00ae\3\2\2\2\36\u00bb\3\2\2\2 \u00ee\3\2\2\2\"\u00fa\3\2"+
		"\2\2$\u00fd\3\2\2\2&\u0110\3\2\2\2(\u0120\3\2\2\2*\u0126\3\2\2\2,\u0135"+
		"\3\2\2\2.\u0142\3\2\2\2\60\u0155\3\2\2\2\62\u0164\3\2\2\2\64\u016d\3\2"+
		"\2\2\66\u0178\3\2\2\289\7\37\2\29:\78\2\2:;\7\36\2\2;<\5\4\3\2<=\5\16"+
		"\b\2=>\5\66\34\2>\3\3\2\2\2?A\7,\2\2@B\5\6\4\2A@\3\2\2\2BC\3\2\2\2CA\3"+
		"\2\2\2CD\3\2\2\2D\5\3\2\2\2EF\5\b\5\2FG\7\35\2\2GL\5\f\7\2HI\7\34\2\2"+
		"IK\5\f\7\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2"+
		"OP\7\36\2\2P\7\3\2\2\2QR\t\2\2\2R\t\3\2\2\2ST\t\3\2\2T\13\3\2\2\2U_\7"+
		"8\2\2VW\7\25\2\2WX\7\64\2\2X`\7\26\2\2YZ\7\25\2\2Z[\7\64\2\2[\\\7\26\2"+
		"\2\\]\7\25\2\2]^\7\64\2\2^`\7\26\2\2_V\3\2\2\2_Y\3\2\2\2_`\3\2\2\2`\r"+
		"\3\2\2\2ac\5\20\t\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e\17\3\2\2"+
		"\2fg\7!\2\2gh\5\22\n\2hi\78\2\2ij\b\t\1\2jl\7\23\2\2km\5\24\13\2lk\3\2"+
		"\2\2lm\3\2\2\2mn\3\2\2\2np\7\24\2\2oq\5\4\3\2po\3\2\2\2pq\3\2\2\2qr\3"+
		"\2\2\2rt\7\27\2\2su\5\"\22\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\30\2\2"+
		"w\21\3\2\2\2xy\t\4\2\2y\23\3\2\2\2z{\5\b\5\2{|\78\2\2|\u0084\b\13\1\2"+
		"}~\7\34\2\2~\177\5\b\5\2\177\u0080\78\2\2\u0080\u0081\b\13\1\2\u0081\u0083"+
		"\3\2\2\2\u0082}\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084"+
		"\u0085\3\2\2\2\u0085\25\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u008c\5\30\r"+
		"\2\u0088\u0089\7\f\2\2\u0089\u008b\5\30\r\2\u008a\u0088\3\2\2\2\u008b"+
		"\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\27\3\2\2"+
		"\2\u008e\u008c\3\2\2\2\u008f\u0099\5\32\16\2\u0090\u0091\7\r\2\2\u0091"+
		"\u0095\b\r\1\2\u0092\u0093\7\16\2\2\u0093\u0095\b\r\1\2\u0094\u0090\3"+
		"\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\5\32\16\2\u0097"+
		"\u0094\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2"+
		"\2\2\u009a\31\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u00ac\5\34\17\2\u009d"+
		"\u009e\7\7\2\2\u009e\u00aa\b\16\1\2\u009f\u00a0\7\6\2\2\u00a0\u00aa\b"+
		"\16\1\2\u00a1\u00a2\7\t\2\2\u00a2\u00aa\b\16\1\2\u00a3\u00a4\7\b\2\2\u00a4"+
		"\u00aa\b\16\1\2\u00a5\u00a6\7\13\2\2\u00a6\u00aa\b\16\1\2\u00a7\u00a8"+
		"\7\n\2\2\u00a8\u00aa\b\16\1\2\u00a9\u009d\3\2\2\2\u00a9\u009f\3\2\2\2"+
		"\u00a9\u00a1\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a7"+
		"\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\5\34\17\2\u00ac\u00a9\3\2\2\2"+
		"\u00ac\u00ad\3\2\2\2\u00ad\33\3\2\2\2\u00ae\u00b8\5\36\20\2\u00af\u00b0"+
		"\7\17\2\2\u00b0\u00b4\b\17\1\2\u00b1\u00b2\7\20\2\2\u00b2\u00b4\b\17\1"+
		"\2\u00b3\u00af\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7"+
		"\5\36\20\2\u00b6\u00b3\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2"+
		"\u00b8\u00b9\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00c5"+
		"\5 \21\2\u00bc\u00bd\7\21\2\2\u00bd\u00c1\b\20\1\2\u00be\u00bf\7\22\2"+
		"\2\u00bf\u00c1\b\20\1\2\u00c0\u00bc\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1"+
		"\u00c2\3\2\2\2\u00c2\u00c4\5 \21\2\u00c3\u00c0\3\2\2\2\u00c4\u00c7\3\2"+
		"\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\37\3\2\2\2\u00c7\u00c5"+
		"\3\2\2\2\u00c8\u00ef\5\n\6\2\u00c9\u00ca\7\23\2\2\u00ca\u00cb\b\21\1\2"+
		"\u00cb\u00cc\5\26\f\2\u00cc\u00cd\7\24\2\2\u00cd\u00ce\b\21\1\2\u00ce"+
		"\u00ef\3\2\2\2\u00cf\u00ec\78\2\2\u00d0\u00ed\3\2\2\2\u00d1\u00ed\t\5"+
		"\2\2\u00d2\u00d3\7\25\2\2\u00d3\u00d4\5\30\r\2\u00d4\u00d5\7\26\2\2\u00d5"+
		"\u00ed\3\2\2\2\u00d6\u00d7\7\25\2\2\u00d7\u00d8\5\30\r\2\u00d8\u00d9\7"+
		"\26\2\2\u00d9\u00da\7\25\2\2\u00da\u00db\5\30\r\2\u00db\u00dc\7\26\2\2"+
		"\u00dc\u00ed\3\2\2\2\u00dd\u00de\7\23\2\2\u00de\u00e8\b\21\1\2\u00df\u00e9"+
		"\3\2\2\2\u00e0\u00e5\5\26\f\2\u00e1\u00e2\7\34\2\2\u00e2\u00e4\5\26\f"+
		"\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6"+
		"\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00df\3\2\2\2\u00e8"+
		"\u00e0\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\7\24\2\2\u00eb\u00ed\b"+
		"\21\1\2\u00ec\u00d0\3\2\2\2\u00ec\u00d1\3\2\2\2\u00ec\u00d2\3\2\2\2\u00ec"+
		"\u00d6\3\2\2\2\u00ec\u00dd\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00c8\3\2"+
		"\2\2\u00ee\u00c9\3\2\2\2\u00ee\u00cf\3\2\2\2\u00ef!\3\2\2\2\u00f0\u00f9"+
		"\5$\23\2\u00f1\u00f9\5&\24\2\u00f2\u00f9\5(\25\2\u00f3\u00f9\5,\27\2\u00f4"+
		"\u00f9\5.\30\2\u00f5\u00f9\5\60\31\2\u00f6\u00f9\5\62\32\2\u00f7\u00f9"+
		"\5\64\33\2\u00f8\u00f0\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f8\u00f2\3\2\2\2"+
		"\u00f8\u00f3\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f8\u00f6"+
		"\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa"+
		"\u00fb\3\2\2\2\u00fb#\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u010a\78\2\2\u00fe"+
		"\u010b\3\2\2\2\u00ff\u0100\7\25\2\2\u0100\u0101\5\30\r\2\u0101\u0102\7"+
		"\26\2\2\u0102\u010b\3\2\2\2\u0103\u0104\7\25\2\2\u0104\u0105\5\30\r\2"+
		"\u0105\u0106\7\26\2\2\u0106\u0107\7\25\2\2\u0107\u0108\5\30\r\2\u0108"+
		"\u0109\7\26\2\2\u0109\u010b\3\2\2\2\u010a\u00fe\3\2\2\2\u010a\u00ff\3"+
		"\2\2\2\u010a\u0103\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7\f\2\2\u010d"+
		"\u010e\5\26\f\2\u010e\u010f\7\36\2\2\u010f%\3\2\2\2\u0110\u0111\78\2\2"+
		"\u0111\u011b\7\23\2\2\u0112\u011c\3\2\2\2\u0113\u0118\5\30\r\2\u0114\u0115"+
		"\7\34\2\2\u0115\u0117\5\30\r\2\u0116\u0114\3\2\2\2\u0117\u011a\3\2\2\2"+
		"\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118"+
		"\3\2\2\2\u011b\u0112\3\2\2\2\u011b\u0113\3\2\2\2\u011c\u011d\3\2\2\2\u011d"+
		"\u011e\7\24\2\2\u011e\u011f\7\36\2\2\u011f\'\3\2\2\2\u0120\u0121\7\"\2"+
		"\2\u0121\u0122\7\23\2\2\u0122\u0123\5\26\f\2\u0123\u0124\7\24\2\2\u0124"+
		"\u0125\7\36\2\2\u0125)\3\2\2\2\u0126\u0133\78\2\2\u0127\u0134\3\2\2\2"+
		"\u0128\u0129\7\25\2\2\u0129\u012a\5\30\r\2\u012a\u012b\7\26\2\2\u012b"+
		"\u0134\3\2\2\2\u012c\u012d\7\25\2\2\u012d\u012e\5\30\r\2\u012e\u012f\7"+
		"\26\2\2\u012f\u0130\7\25\2\2\u0130\u0131\5\30\r\2\u0131\u0132\7\26\2\2"+
		"\u0132\u0134\3\2\2\2\u0133\u0127\3\2\2\2\u0133\u0128\3\2\2\2\u0133\u012c"+
		"\3\2\2\2\u0134+\3\2\2\2\u0135\u0136\7#\2\2\u0136\u0137\7\23\2\2\u0137"+
		"\u013c\5*\26\2\u0138\u0139\7\34\2\2\u0139\u013b\5*\26\2\u013a\u0138\3"+
		"\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d"+
		"\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\7\24\2\2\u0140\u0141\7"+
		"\36\2\2\u0141-\3\2\2\2\u0142\u0143\7$\2\2\u0143\u0146\7\23\2\2\u0144\u0147"+
		"\5\26\f\2\u0145\u0147\7\66\2\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2"+
		"\u0147\u014f\3\2\2\2\u0148\u014b\7\34\2\2\u0149\u014c\5\26\f\2\u014a\u014c"+
		"\7\66\2\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\u014e\3\2\2\2"+
		"\u014d\u0148\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150"+
		"\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\7\24\2\2"+
		"\u0153\u0154\7\36\2\2\u0154/\3\2\2\2\u0155\u0156\7%\2\2\u0156\u0157\7"+
		"\23\2\2\u0157\u0158\5\30\r\2\u0158\u0159\7\24\2\2\u0159\u015a\7&\2\2\u015a"+
		"\u015b\7\27\2\2\u015b\u015c\5\"\22\2\u015c\u0162\7\30\2\2\u015d\u015e"+
		"\7\'\2\2\u015e\u015f\7\27\2\2\u015f\u0160\5\"\22\2\u0160\u0161\7\30\2"+
		"\2\u0161\u0163\3\2\2\2\u0162\u015d\3\2\2\2\u0162\u0163\3\2\2\2\u0163\61"+
		"\3\2\2\2\u0164\u0165\7(\2\2\u0165\u0166\7\23\2\2\u0166\u0167\5\30\r\2"+
		"\u0167\u0168\7\24\2\2\u0168\u0169\7)\2\2\u0169\u016a\7\27\2\2\u016a\u016b"+
		"\5\"\22\2\u016b\u016c\7\30\2\2\u016c\63\3\2\2\2\u016d\u016e\7*\2\2\u016e"+
		"\u016f\5*\26\2\u016f\u0170\7\f\2\2\u0170\u0171\5\30\r\2\u0171\u0172\7"+
		"+\2\2\u0172\u0173\5\30\r\2\u0173\u0174\7)\2\2\u0174\u0175\7\27\2\2\u0175"+
		"\u0176\5\"\22\2\u0176\u0177\7\30\2\2\u0177\65\3\2\2\2\u0178\u0179\7 \2"+
		"\2\u0179\u017a\7\23\2\2\u017a\u017b\7\24\2\2\u017b\u017c\7\27\2\2\u017c"+
		"\u017d\5\"\22\2\u017d\u017e\7\30\2\2\u017e\67\3\2\2\2\"CL_dlpt\u0084\u008c"+
		"\u0094\u0099\u00a9\u00ac\u00b3\u00b8\u00c0\u00c5\u00e5\u00e8\u00ec\u00ee"+
		"\u00f8\u00fa\u010a\u0118\u011b\u0133\u013c\u0146\u014b\u014f\u0162";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}