<!--
.. title: C++ 对象模型
.. slug: c++-dui-xiang-mo-xing
.. date: 2016-09-26 13:33:14 UTC+08:00
.. tags: c++
.. category: 
.. link:
.. description:
.. type: text
-->
[toc]

我觉得学习中最幸福的时刻是 "aha moment": 当你弄懂一个思考很久的知识点，然后发现以前郁结于心的很多问题都解释得通了的那一刻。在我学习C++的经历中，印象最深的"aha moment"当属弄懂对象模型的时刻,因此当我想写关于C++的博客时，我决定利用"贪婪算法":先写我觉得最有趣的东西。

*本篇博客中的例子都是用 clang3.5在 MacOSX 10.11 64位下编译得到，有些例子在不同的系统和编译器下可能结果不同*

C++ 中最简单的对象类型是 Plain Old Data (POD)类型，例如下面这个结构体：
```c++
struct toy{
    int a;
    int b;
}
```



这样的结构体和C语言的结构体别无二致,它没有构造函数和析构函数，它包含的数据都是原始类型，它也没有继承别的类。像上面的这种C++结构体是和C兼容的，可以用C语言的内存函数如`memcpy，memset`来操作这个结构体。它的内存布局也相对简单，结构体的大小就是结构体内元素的大小加上内存对齐。比如上面的toy这个结构体，用`sizeof(toy)`可以得到它的大小为8(Bytes),即两个`int`型变量的大小的和，如果把toy里b的类型改为`char`型，虽然一个`int`加上一个`char`大小是5，但是由于内存对齐的要求，仍然要为toy分配8字节的内存，C++标准要求类中的数据布局和变量的声明顺序一致，在toy 中，由于a先声明，b后声明，在toy的实例中，a也要在前，b在后，地址由低到高。这里面隐藏的一个问题是，由于a占了前4个字节，b 只占一个字节，它在后面4个字节任何位置都是对齐的，那么编译器会把b放在哪里呢？可以用下面的程序验证：

```c++

#include<iostream>
struct toy{
    int a;
    char b;
};
int main (){
    toy t;
    t.b = 'a';
    char* p = reinterpret_cast<char*>(&t);
    for(size_t i=0;i<4;++i)
        std::cout<<i+5<<":"<<p[i+4]<<" ";
    return 0;

 /*输出:
    5:a 6: 7: 8:
 */
}
```
上面的程序输出了t从第5个字节起的所有值，注意 6,7,8内存位置都是不可打印的值，5号位置是程序main函数第二行写入b的值。也就是说b的内存是在后四个字节的起始位置。另一种情况是，如果在toy中再增加一个`int16_t` 类型的数据，它是在第6,7个字节吗？注意这个时候由于它是需要对齐的，它的大小是2个字节，因此它应该对齐在第7个字节的内存位置。第6号位置就被跳过了，这时的toy内存布局为:
```c++
address:| 0 | 1 | 2 | 3 |  4  | 5 | 6 | 7 |
    toy{|      int      | char|   |int16_t|}
```
<!-- TEASER_END -->
数据对齐加快内存读写速度的同时也使得内存空间的产生了一定的浪费，toy结构体浪费了3/8的内存空间，如果在程序需要实例化很多toy的对象，浪费的空间总量是很可观的。好在很多编译器都提供了选项来紧凑的表示结构体，比如 gcc 和clang提供了 `__attribute__((packed))`，如果对上面的toy 例子使用这个属性，它所占内存将变为5。

现在来看C++ 的类变量。如果类中有虚函数，那么C++会为每个类创建一个虚函数表(vtable),对于类的每个实例，C++都默认创建一个虚函数指针,放在对象的起始位置,如果在上面的toy中加入一个虚函数:
```c++
class toy {
    int a;
    char b;
public:
    virtual void foo(){
    std::cout<<"toy::foo";
    }
}
```
在64位系统下，一个指针占用8字节，故上面的toy的大小是16字节(别忘了内存对齐),把上述类写成C语言的的伪代码就是:

```c
struct toy{
    void* vtbl;
    int a;
    char b;
}
/*虚函数表:
vtbl--->{toy::foo}
*/
```

比这更复杂的情况是，如果一个子类继承了带有虚函数的父类，那么它的大小是多少？如果是多重继承呢？比如下面这个例子：
```c++
class Base1 {
public:
    virtual void foo() {
    cout << "Base1::foo" << endl;
    }
    virtual void foo2(){
    cout << "Base1::foo2" << endl;
    }
};
class Base2{
public:
    virtual void bar() {
    cout << "Base2::bar" << endl;
    }
    virtual void bar2(){
    cout << "Base2::bar2" << endl;
    }
};
class Derive : public Base1,public Base2{
    int v;
};

```
在这种情况下，现有C++编译的做法是父类中有几个带有虚函数就在子类中放置几个虚函数指针，每个指针分别指向一个夫类虚函数的地址，安装继承的声明顺序从前往后排列。根据这个规则，上面的 Derive 可以翻译成下面的伪代码:
```c++
struct Dervie{
    void* vtbl_base1//指向Base1 的虚函数表
    void* vtbl_base2//指向Base2 的虚函数表
    int v;
}
/*虚函数表:
vtabl_base1----> {Base1::foo,Base1::foo2}
vtabl_base2----> {Base2::bar,Base2::bar2}
*/
```

既然虚函数表在对象的起始位置,那么我们应该可以通过读取对象的前8个字节（注意到在64位机器上指针是8个字节）来得到Base1的虚函数表地址，第9-16个字节来得到Base2的虚函数表地址。得到虚函数表地址后可以直接通过虚函数表来得到函数地址,进而调用这个函数：
```c++
#include <iostream>
using namespace std;
class Base1 {
public:
    virtual void foo() {
    cout << "Base1::foo" << endl;
    }
    virtual void foo2(){
    cout << "Base1::foo2" << endl;
    }
};
class Base2{
public:
    virtual void bar() {
    cout << "Base2::bar" << endl;
    }
    virtual void bar2(){
    cout << "Base2::bar2" << endl;
    }
};
class Derive : public Base1,public Base2{
    int v;
};

//获取虚函数的地址
template<typename T> void*
get_vfunc_addr(T&& obj,int vtbl_idx=0,
                int func_idx=0){
    //获得 obj 的地址
     int64_t * p = (int64_t*)&obj;
    //获得第 vtbl_idx 个虚函数表的地址
    int64_t* vtbl = (int64_t*)p[vtbl_idx];
    //获得虚函数表中第 func_idx 个函数的指针
    return (void*)vtbl[func_idx];
}

using Fptr = void(*)();
int main() {
 Base1 b1;
 Base2 b2;
 Derive d;
 for (int i = 0; i < 2; ++i) {
  for (int j = 0; j < 2; ++j) {
   //得到derive 第i个虚函数的第j个函
   //数的地址并转换成函数指针
    Fptr func=(Fptr)get_vfunc_addr(d,i,j);
    //调用这个函数
    func();
  }
 }
 return 0;
}
/*
输出：
Base1::foo
Base1::foo2
Base2::bar
Base2::bar2
*/
```
在 `get_vfunc_addr` 这个函数里，我们先获得传入的对象的地址，由于指针大小是8个字节，我们把对象地址转换为int64_t类型的指针，然后在解引用时我们就得到了一个8字节大小的数据，它代表的是虚函数表的首地址，既然虚函数表中存储的函数指针，因此表中每个单元的大小也是8字节，因此我们再将首地址转换为int64_t类型的指针,这样解引用时我们就得到了8字节的函数指针，得到了函数指针，把它转换回原有函数类型，就可以调用这个函数了。

获得虚函数似乎并没有用，因为在代码中我们总是可以利用指针和引用轻易调用虚函数。下面设想如果有一个类,我们需要修改它的某个属性,但是这个类并没有相应接口，如果这个属性恰好不是`public`的，C++中按常规办法是不能修改它了，但是利用对象的内存布局，我们完全可以**绕过C++ 的访问限定规则，在类外部访问私有变量**，比如下面的Student类中，我们要修改`name_`的值：
```c++
#include <iostream>

class Student{
public:
 int a;
 char b;
 void set(char* v){ name_ = v; }
 void print(){
 std::cout<<"my name is "<<name_<<"\n";
 }
private:
    char* name_;
};

int main() {
 std::cout<<sizeof(Student)<<std::endl;
 Student t;
 char name[] = "Han mei mei";
 t.set(name);
 char* p = (char*)&t;
 t.print();
 char* tmp = (char*)(*((int64_t *)(p+8)));
 fgets(tmp,strlen(tmp),stdin);
 t.print();
 return 0;
}
/*
输入:
li lei
输出:
my name is Han mei mei
my name is li lei
*/
```
在main函数的第一行，打印出Student的大小是16，由于name\_的大小是8字节，因此它一定在第9-16个字节。我们通过指针地址对象t的首地址加上8个字节,即(p+8)，先得到`name_`的首地址，然后通过解引用得到了`name_`的值，最后把它转换回它原来的类型`char*`指针，这样我们就得到了Student的私有数据`name_`，得到这个指针过后要修改它就很容易了。


