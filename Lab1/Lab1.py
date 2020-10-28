/*�������� ������ ��-02
����������� ������ 1
������ 34*/
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    float a; //����� ����� ����
    std::cout << "������� ����� ����� ����: ";
    std::cin >> a; 
    float s = 4 * a * a; //���������� ������� ������� �����������
    float v = a * a * a; //���������� ������
    std::cout << "������� ������� ����������� : " << s << std::endl;
    std::cout << "����� ���� : " << v << std::endl;

        system("pause");
    return 0;
}