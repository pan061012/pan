import random
import string


def get_char_pool(choice):
    """根据用户选择返回对应的字符池"""
    if choice == 1:
        return string.digits
    elif choice == 2:
        return string.digits + string.ascii_letters
    elif choice == 3:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.?/~`"
        return string.digits + string.ascii_letters + special_chars
    return ""


def generate_password(length, char_pool):
    """生成指定长度的随机密码，字符不重复"""
    max_length = len(char_pool)
    if length > max_length:
        print(f"⚠️ 密码长度超过可选字符数量，已自动调整为字符池最大长度 {max_length}")
        length = max_length
    return ''.join(random.sample(char_pool, length))


def get_valid_length():
    """获取并验证用户输入的密码长度"""
    while True:
        user_input = input("请输入想要生成的密码长度：")
        if not user_input.isdigit():
            print("❌ 请输入有效的正整数！")
            continue
        length = int(user_input)
        if length <= 0:
            print("❌ 密码长度必须为正整数，请重新输入！")
            continue
        return length


def get_valid_choice():
    """获取并验证用户选择的密码类型"""
    print("\n请选择密码组成类型：")
    print("选项 1：仅数字（0-9）")
    print("选项 2：数字 + 大小写字母")
    print("选项 3：数字 + 大小写字母 + 特殊符号")
    while True:
        user_input = input("请输入选项（1/2/3）：")
        if not user_input.isdigit() or user_input not in ['1', '2', '3']:
            print("❌ 请选择 1、2、3 中的一个选项！")
            continue
        return int(user_input)


def get_continue_choice():
    """获取并验证用户是否继续的选择"""
    while True:
        user_input = input("\n是否继续生成新密码？(Y/N)：").strip().upper()
        if user_input in ['Y', 'N']:
            return user_input == 'Y'
        print("❌ 请输入 Y（继续）或 N（退出）！")


def main():
    print("=" * 40)
    print("随机密码生成器")
    print("=" * 40)
    
    while True:
        length = get_valid_length()
        choice = get_valid_choice()
        char_pool = get_char_pool(choice)
        password = generate_password(length, char_pool)
        print(f"\n✅ 生成的随机密码：{password}")
        
        if not get_continue_choice():
            print("\n👋 感谢使用随机密码生成器！")
            break
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
