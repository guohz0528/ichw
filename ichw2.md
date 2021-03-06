## 作业2
1.停机问题

图灵证明停机问题，是为了证明对于图灵机而言，存在着不可判定的问题类。说明了程序不是无所不能的。

图灵证明停机问题采用了对角线方法。设存在判定停机问题的通用算法H，设K(H)，当H输出可停机时K不停机，当H输出不停机时不停机。则对程序K(H(K))，若K停机则K不停机，若K停机则K不停机，产生矛盾。从而说明了不存在判定停机问题的通用算法，图灵机存在不可判定的问题。

停机问题体现了一阶逻辑的不自洽性和不完备性。

2.二进制补码

为简化电路设计和运算步骤，将减法运算合并入加法运算，而采用二进制补码。16bit整数n>=0时，补码与原码相同，n<0时，补码符号位为1，补码后15位与原码后15位和为2^15。将减法运算表示成被减数与减数的相反数的和，差即为和的补码。

原理上，原码后15位的相反数与补码后15位摩2^15同余，而如果和有进位，则与符号位的1抵消，从而差即为和的补码。

3.浮点数

Sign | Exp | Frac | Value
-----|-----|------|------
0or1|0000000|00000000|±0.0 
0or1|0111111|00000000|±1.0 
0or1|0000000|00000001|\(±2^{-8} × 2^{−62} \) (最小非规范化数)
0or1|0000000|11111111|\(±(1−2^{−8}) × 2^{−62}\) (最大非规范化数) 
0or1|1111111|00000000|±∞ 
0or1|1111111|non zero|NaN 
0or1|0000001|00000000|\(±2^{−62}\) (最小规范化浮点数)  
0or1|1111110|11111111|\(±(2−2^{−8}) × 2^{63}\) (最大规范化浮点数)
