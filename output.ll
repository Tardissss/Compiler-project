; ModuleID = "/home/shensy/Documents/Complier/project/Compiler-project/codegen.pyc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = icmp sle i8 1, 2
  %".3" = bitcast [5 x i8]* @"fstr<ast.Less_equal instance at 0x7fcd802db170>" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i1 %".2")
  %".5" = icmp sge i8 1, 2
  %".6" = bitcast [5 x i8]* @"fstr<ast.Greater_equal instance at 0x7fcd802db320>" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i1 %".5")
  %".8" = icmp sgt i8 1, 2
  %".9" = bitcast [5 x i8]* @"fstr<ast.Greater instance at 0x7fcd802db368>" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i1 %".8")
  %".11" = icmp slt i8 1, 2
  %".12" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7fcd80306d88>" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i1 %".11")
  %".14" = icmp ne i8 1, 2
  %".15" = bitcast [5 x i8]* @"fstr<ast.Not_equal instance at 0x7fcd80306ea8>" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i1 %".14")
  %".17" = icmp eq i8 1, 2
  %".18" = bitcast [5 x i8]* @"fstr<ast.Equal instance at 0x7fcd80306fc8>" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i1 %".17")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr<ast.Less_equal instance at 0x7fcd802db170>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater_equal instance at 0x7fcd802db320>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater instance at 0x7fcd802db368>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7fcd80306d88>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Not_equal instance at 0x7fcd80306ea8>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Equal instance at 0x7fcd80306fc8>" = internal constant [5 x i8] c"%i \0a\00"