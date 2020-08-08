# 字符串匹配暴力法代码示例
```Python3
def forceSearch(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n-m+1):
    for j in range(m):
        if txt[i+j] != pat[j]:
        break
    if j == m:
        return i
    return -1 
```
```Java
public static int forceSearch(String txt, String pat) {
    int M = txt.length();
    int N = pat.length();
    for (int i = 0; i <= M - N; i++) {
        int j;
        for (j = 0; j < N; j++) {
            if (txt.charAt(i + j) != pat.charAt(j))
                break;
        }
        if (j == N) {
            return i;
        }
        // 更加聪明？ 
        // 1. 预先判断 hash(txt.substring(i, M)) == hash(pat)
        // 2. KMP 
    }
    return -1;
}
```
```JavaScript
function bf(text, pattern) {
  let n = text.length;
  let m = pattern.length;
  for (let i = 0; i < n - m + 1; i++) {
    let matched = true;
    for (let j = 0; j < m; j++) {
      if (source[i + j] !== pattern[j]) {
        matched = false;
        break;
      }
    }
    if (matched) return true;
  }
  return false;
}

console.log(bf("abcabcabx", "abcabx"));
```

# Rabin-Karp 代码示例
```Python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = 256
        q = 9997
        n = len(haystack)
        m = len(needle)
        h = pow(d,m-1)%q
        p = 0
        t = 0
        if m > n:
            return -1
        for i in range(m): # preprocessing
            p = (d*p+ord(needle[i]))%q
            t = (d*t+ord(haystack[i]))%q
        for s in range(n-m+1): # note the +1
            if p == t: # check character by character
                match = True
                for i in range(m):
                    if needle[i] != haystack[s+i]:
                        match = False
                        break
                if match:
                    return s
            if s < n-m:
                t = (t-h*ord(haystack[s]))%q
                t = (t*d+ord(haystack[s+m]))%q
                t = (t+q)%q
        return -1
```
```
public final static int D = 256;
public final static int Q = 9997;

static int RabinKarpSerach(String txt, String pat) {
    int M = pat.length();
    int N = txt.length();
    int i, j;
    int patHash = 0, txtHash = 0;

    for (i = 0; i < M; i++) {
        patHash = (D * patHash + pat.charAt(i)) % Q;
        txtHash = (D * txtHash + txt.charAt(i)) % Q;
    }

    int highestPow = 1;  // pow(256, M-1)
    for (i = 0; i < M - 1; i++) 
        highestPow = (highestPow * D) % Q;

    for (i = 0; i <= N - M; i++) { // 枚举起点
        if (patHash == txtHash) {
            for (j = 0; j < M; j++) {
                if (txt.charAt(i + j) != pat.charAt(j))
                    break;
            }
            if (j == M)
                return i;
        }
        if (i < N - M) {
            txtHash = (D * (txtHash - txt.charAt(i) * highestPow) + txt.charAt(i + M)) % Q;
            if (txtHash < 0)
                txtHash += Q;
        }
    }

    return -1;
}
```

```JavaScript
function rabinKarpSearch(text, pattern) {
  const D = 256;
  const Q = 9997;

  let N = text.length;
  let M = pattern.length;
  let patHash = 0;
  let txtHash = 0;

  for (let i = 0; i < M; i++) {
    patHash = (D * patHash + pattern[i].codePointAt(0)) % Q;
    txtHash = (D * txtHash + text[i].codePointAt(0)) % Q;
  }

  let highestPow = 1; // 256 ** (M - 1);
  for (let i = 0; i < M - 1; i++) {
    highestPow = (highestPow * D) % Q;
  }

  let i, j;
  for (i = 0; i < N - M + 1; i++) {
    if (patHash === txtHash) {
      for (j = 0; j < M; j++) {
        if (pattern[j] !== text[i + j]) break;
      }
      if (j === M) return i;
    }
    if (i < N - M) {
      txtHash = (D * (txtHash - text[i].codePointAt(0) * highestPow) + text[i + M].codePointAt(0)) % Q;
      if (txtHash < 0) {
        txtHash += Q;
      }
    }
  }
  return -1;
}

console.log(rabinKarpSearch("abcabcabx", "abcabx"));
```