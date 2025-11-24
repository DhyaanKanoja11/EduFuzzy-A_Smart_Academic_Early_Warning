% =======================================================================
% PROJECT: EduFuzzy (Logic Module)
% DOMAIN: Student Performance Risk Analysis
% AUTHOR: Dhyaan Kanoja
% =======================================================================

% ------------------------------------------------------------------------------
% 1. KNOWLEDGE BASE (FACTS)
% Format: student(ID, Name, Attendance_Percent, Internal_Marks).
% ------------------------------------------------------------------------------
student(101, alice, 85, 42).
student(102, bob, 60, 25).
student(103, charlie, 95, 48).
student(104, david, 40, 15).
student(105, eve, 75, 35).
student(106, frank, 20, 10).
student(107, grace, 88, 39).
student(108, hannah, 55, 28).

% ------------------------------------------------------------------------------
% 2. FUZZY SET DEFINITIONS (CRISP APPROXIMATION)
% We define ranges to simulate the "Low/Medium/High" fuzzy sets.
% ------------------------------------------------------------------------------

% --- Attendance Rules ---
attendance_low(A)    :- A < 50.
attendance_medium(A) :- A >= 50, A < 75.
attendance_high(A)   :- A >= 75.

% --- Internal Marks Rules (Max 50) ---
marks_poor(M)    :- M < 25.
marks_average(M) :- M >= 25, M < 40.
marks_good(M)    :- M >= 40.

% ------------------------------------------------------------------------------
% 3. INFERENCE RULES (THE "BRAIN")
% These match the rules defined in your Python RuleBase.py
% ------------------------------------------------------------------------------

% Rule 1 & 4: Critical Risk
% IF Attendance is Low OR Marks are Poor -> Risk is Critical
risk_status(A, M, 'Critical') :-
    attendance_low(A);
    marks_poor(M).

% Rule 2: Monitor Risk
% IF Attendance is Medium AND Marks are Average -> Risk is Monitor
risk_status(A, M, 'Monitor') :-
    attendance_medium(A),
    marks_average(M).

% Rule 3: Safe
% IF Attendance is High OR Marks are Good -> Risk is Safe
% (We use a cut ! to prevent backtracking if previous rules failed but this one matches)
risk_status(A, M, 'Safe') :-
    attendance_high(A);
    marks_good(M).

% Fallback Rule
risk_status(_, _, 'Unknown').

% ------------------------------------------------------------------------------
% 4. QUERY HELPERS
% ------------------------------------------------------------------------------

% Analyze a specific student by Name
analyze_student(Name) :-
    student(ID, Name, Att, Marks),
    risk_status(Att, Marks, Status),
    format('Student: ~w (ID: ~w)~n', [Name, ID]),
    format('  Attendance: ~w%~n', [Att]),
    format('  Marks: ~w/50~n', [Marks]),
    format('  Risk Prediction: ~w~n', [Status]),
    nl.

% Analyze ALL students in the database
report_all :-
    write('--- EDUFUZZY CLASS REPORT ---'), nl,
    student(ID, Name, Att, Marks),
    risk_status(Att, Marks, Status),
    format('~w | ~w% | ~w | ~w', [Name, Att, Marks, Status]), nl,
    fail. % Force backtracking to find next student
report_all.
