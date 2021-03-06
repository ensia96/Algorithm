import java.util.*;

public class Main {

	public static int n;
	public static ArrayList<Integer> arrayList = new ArrayList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			arrayList.add(sc.nextInt());
		}
		Collections.sort(arrayList);

		int result = 0; // 총 그룹의 수
		int count = 0;// 현재 그룹에 포함된 모험가의 수
		// 공포도를 낮은 것부터 하나씩 확인하며
		for (int i = 0; i < n; i++) {
			count += 1; // 현재 그룹에 해당 모험가를 포함시키기
			// 모험가의 수가 현재의 공포도 이상이라면,
			if (count >= arrayList.get(i)) {
				result += 1; // 그룹을 결성 (총 그룹의 수 증가시키기)
				count = 0; // 현재 그룹에 포함된 모험가의 수 초기화
			}
		}
		System.out.println(result);
	}
} 