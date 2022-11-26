totalSeconds = int(input('請輸入秒數: '))

hours = totalSeconds // (60 * 60)
remainSeconds = totalSeconds % (60 * 60)
minutes = remainSeconds // 60
seconds = remainSeconds % 60

print(f'{hours}時{minutes}分{seconds}秒')
