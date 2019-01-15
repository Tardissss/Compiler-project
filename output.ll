; ModuleID = "/home/shensy/Documents/Complier/project/Compiler-project/codegen.pyc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = icmp sle i8 1, 2
  %".3" = bitcast [5 x i8]* @"fstr<ast.Less_equal instance at 0x7f597d92eef0>" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i1 %".2")
  %".5" = icmp sge i8 1, 2
  %".6" = bitcast [5 x i8]* @"fstr<ast.Greater_equal instance at 0x7f597d92ef80>" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i1 %".5")
  %".8" = icmp sgt i8 1, 2
  %".9" = bitcast [5 x i8]* @"fstr<ast.Greater instance at 0x7f597d92e878>" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i1 %".8")
  %".11" = icmp sgt i8 1, 3
  br i1 %".11", label %"entry.if", label %"entry.else"
entry.if:
  %".13" = icmp sle i8 1, 2
  %".14" = bitcast [5 x i8]* @"fstr<ast.Less_equal instance at 0x7f597d929f80>" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i1 %".13")
  %".16" = icmp sge i8 1, 2
  %".17" = bitcast [5 x i8]* @"fstr<ast.Greater_equal instance at 0x7f597d936cb0>" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i1 %".16")
  %".19" = icmp sgt i8 1, 2
  %".20" = bitcast [5 x i8]* @"fstr<ast.Greater instance at 0x7f597d936128>" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i1 %".19")
  br label %"entry.endif"
entry.else:
  %".23" = icmp slt i8 1, 2
  %".24" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7f597d9362d8>" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i1 %".23")
  %".26" = icmp ne i8 1, 2
  %".27" = bitcast [5 x i8]* @"fstr<ast.Not_equal instance at 0x7f597d936488>" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i1 %".26")
  %".29" = icmp eq i8 1, 2
  %".30" = bitcast [5 x i8]* @"fstr<ast.Equal instance at 0x7f597d9365a8>" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i1 %".29")
  br label %"entry.endif"
entry.endif:
  %".33" = icmp slt i8 1, 2
  %".34" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7f597d8dffc8>" to i8*
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34", i1 %".33")
  %".36" = icmp ne i8 1, 2
  %".37" = bitcast [5 x i8]* @"fstr<ast.Not_equal instance at 0x7f597d94bb00>" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i1 %".36")
  %".39" = icmp eq i8 1, 2
  %".40" = bitcast [5 x i8]* @"fstr<ast.Equal instance at 0x7f597d94de60>" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i1 %".39")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr<ast.Less_equal instance at 0x7f597d92eef0>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater_equal instance at 0x7f597d92ef80>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater instance at 0x7f597d92e878>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less_equal instance at 0x7f597d929f80>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater_equal instance at 0x7f597d936cb0>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater instance at 0x7f597d936128>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7f597d9362d8>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Not_equal instance at 0x7f597d936488>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Equal instance at 0x7f597d9365a8>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7f597d8dffc8>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Not_equal instance at 0x7f597d94bb00>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Equal instance at 0x7f597d94de60>" = internal constant [5 x i8] c"%i \0a\00"