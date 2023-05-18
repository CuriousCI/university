import os

for number in range(2, 21):
    os.mkdir(os.path.join(os.path.dirname(__file__), f'{number}'))

    with open(f'./{number}/Main.java', 'w') as file:
        file.write('''class Main {
	public static void main(String[] args) {

	}
}''')
