; ModuleID = "/home/shensy/Documents/Complier/project/compiler-proj/codegen.pyc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = icmp sgt i8 1, 3
  %".3" = icmp sgt i8 1, 0
  %".4" = and i1 %".2", %".3"
  br i1 %".4", label %"entry.if", label %"entry.else"
entry.if:
  %".6" = icmp sle i8 1, 2
  %".7" = bitcast [5 x i8]* @"fstr<ast.Less_equal instance at 0x7fb21ca5bc20>" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i1 %".6")
  %".9" = icmp sge i8 1, 2
  %".10" = bitcast [5 x i8]* @"fstr<ast.Greater_equal instance at 0x7fb21ca5bd40>" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i1 %".9")
  %".12" = icmp sgt i8 1, 2
  %".13" = bitcast [5 x i8]* @"fstr<ast.Greater instance at 0x7fb21ca5be60>" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i1 %".12")
  br label %"entry.endif"
entry.else:
  %".16" = icmp slt i8 1, 2
  %".17" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7fb21ca5b1b8>" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i1 %".16")
  %".19" = icmp ne i8 1, 2
  %".20" = bitcast [5 x i8]* @"fstr<ast.Not_equal instance at 0x7fb21ca5b248>" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i1 %".19")
  %".22" = icmp eq i8 1, 2
  %".23" = bitcast [5 x i8]* @"fstr<ast.Equal instance at 0x7fb21ca5b518>" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i1 %".22")
  %".25" = icmp sgt i8 1, 3
  %".26" = icmp sgt i8 1, 0
  %".27" = or i1 %".25", %".26"
  br i1 %".27", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ret void
entry.else.if:
  %".29" = icmp slt i8 1, 2
  %".30" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7fb21ca55a28>" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i1 %".29")
  br label %"entry.else.endif"
entry.else.else:
  %".33" = icmp slt i8 1, 2
  %".34" = bitcast [5 x i8]* @"fstr<ast.Less instance at 0x7fb21ca55e18>" to i8*
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34", i1 %".33")
  %".36" = icmp ne i8 1, 2
  %".37" = bitcast [5 x i8]* @"fstr<ast.Not_equal instance at 0x7fb21ca6f200>" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i1 %".36")
  %".39" = icmp eq i8 1, 2
  %".40" = bitcast [5 x i8]* @"fstr<ast.Equal instance at 0x7fb21ca6f128>" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i1 %".39")
  br label %"entry.else.endif"
entry.else.endif:
  br label %"entry.endif"
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr<ast.Less_equal instance at 0x7fb21ca5bc20>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater_equal instance at 0x7fb21ca5bd40>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Greater instance at 0x7fb21ca5be60>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7fb21ca5b1b8>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Not_equal instance at 0x7fb21ca5b248>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Equal instance at 0x7fb21ca5b518>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7fb21ca55a28>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Less instance at 0x7fb21ca55e18>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Not_equal instance at 0x7fb21ca6f200>" = internal constant [5 x i8] c"%i \0a\00"
@"fstr<ast.Equal instance at 0x7fb21ca6f128>" = internal constant [5 x i8] c"%i \0a\00"