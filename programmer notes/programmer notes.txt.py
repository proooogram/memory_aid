.java lib:
	以下有摘录自网上的,也有自己理解总结的,有时有标记,有时没有

Hamcrest:UI验证,数据过滤,单元测试   https://code.google.com/archive/p/hamcrest/wikis/Tutorial.wiki   
	所以Hamcrest的作用是 数据验证(自总结)
	The Hamcrest Tutorial

	Introduction

	Hamcrest is a framework for writing matcher objects allowing 'match' rules to be defined declaratively. There are a number of situations where matchers are invaluble, such as UI validation, or data filtering, but it is in the area of writing flexible tests that matchers are most commonly used. This tutorial shows you how to use Hamcrest for unit testing.

	When writing tests it is sometimes difficult to get the balance right between overspecifying the test (and making it brittle to changes), and not specifying enough (making the test less valuable since it continues to pass even when the thing being tested is broken). Having a tool that allows you to pick out precisely the aspect under test and describe the values it should have, to a controlled level of precision, helps greatly in writing tests that are "just right". Such tests fail when the behaviour of the aspect under test deviates from the expected behaviour, yet continue to pass when minor, unrelated changes to the behaviour are made.



spring boot 作用之一 是自动进行 spring繁杂的配置 以简化spring的使用 (自总结)

jul : java.util.logging 的简写
	所以有 jul-to-slf4j这样的转化库(自总结)
	
	


objenesis:构建实例:Class.newInstance()的替代者并试图弥补其不工作的情形
	To instantiate a new object of a particular class.
	Java already supports this dynamic instantiation of classes using Class.newInstance(). However, this only works if the class has an appropriate constructor. There are many times when a class cannot be instantiated this way, such as when the class contains:

	Constructors that require arguments.
	Constructors that have side effects.
	Constructors that throw exceptions.
	As a result, it is common to see restrictions in libraries stating that classes must require a default constructor. Objenesis aims to overcome these restrictions by bypassing the constructor on object instantiation.
	from : http://objenesis.org/


mockito:...

AspectJ: java的 面向方面AOP 编程
	AspectJ is an aspect-oriented programming (AOP) extension created at PARC for the Java programming language.
	AspectJweaver: AspectJ编织者
	
byte-buddy: java字节码运行时操纵,无需编译器帮助
	Byte Buddy is a code generation and manipulation library for creating and modifying Java classes during the runtime of a Java application and without the help of a compiler	
	

.术语:

Software_release_life_cycle:
	M1:Milestone里程碑1
	RC:Release Candidate:Release候选人
	