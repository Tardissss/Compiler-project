; ModuleID = "/home/shensy/Documents/Complier/project/compiler-proj/codegen.pyc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = mul i8 2, 2
  %".3" = add i8 4, %".2"
  %".4" = bitcast [5 x i8]* @"fstr<ast.Sum instance at 0x7faadb0cb758>" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 %".3")
  %".6" = sdiv i8 8, 4
  %".7" = sub i8 %".6", 2
  %".8" = bitcast [5 x i8]* @"fstr<ast.Sub instance at 0x7faadb0cb908>" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8 %".7")
  %".10" = add i8 4, 4
  %".11" = bitcast [5 x i8]* @"fstr<ast.Sum instance at 0x7faadb0cba28>" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8 %".10")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr<ast.Sum instance at 0x7faadb0cb758>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Sub instance at 0x7faadb0cb908>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Sum instance at 0x7faadb0cba28>" = internal constant [5 x i8] c"%i \0a\00"