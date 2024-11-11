int main() {
    // 输入字符串 s 和模板串 t
    char s[1000], t[1000];
    cin >> s >> t;

    int m = strlen(t); // 模板串 t 的长度
    int n = strlen(s); // 字符串 s 的长度

    // 计算 KMP 的部分匹配表 (next 数组)
    int next[1000];  // next 数组的最大长度为模板串的长度
    next[0] = -1; // next[0] 需要初始化为 -1

    // 计算模板串 t 的 next 数组
    int j = -1; // j 表示模板串 t 当前匹配的位置
    for (int i = 1; i < m; i++) {
        // 根据已经匹配的部分来决定 next[i]
        while (j >= 0 && t[i] != t[j + 1]) {
            j = next[j];  // 回溯
        }
        if (t[i] == t[j + 1]) {
            j++;  // 匹配成功,移动 j
        }
        next[i] = j; // 将 j 保存到 next[i] 中
    }

    // KMP 算法匹配过程
    int i = 0, k = 0; // i 为 s 中的当前字符,k 为 t 中的当前字符
    bool found = false; // 用于判断是否找到匹配的子串

    while (i < n) {
        // 字符匹配,继续比较
        if (s[i] == t[k]) {
            i++;
            k++;
        } else {
            // 如果字符不匹配,则根据 next 数组回溯
            if (k > 0) {
                k = next[k - 1] + 1;
            } else {
                i++;
            }
        }

        // 如果找到了一个匹配
        if (k == m) {
            cout << i - m << " ";  // 输出匹配的起始位置(从0开始索引)
            k = next[k - 1] + 1; // 继续寻找下一个匹配
            found = true;
        }
    }

    // 如果没有找到匹配的子串
    if (!found) {
        cout << "False";
    }

    return 0;
}
