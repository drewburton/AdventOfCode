package day07;

import java.util.*;
import java.io.*;

public class Day07 {
    ArrayList<String> rules;
    HashMap<String, ArrayList<String>> bags;
    
    public Day07() {
        try {
            Scanner scanner = new Scanner(new File("day07\\day7input.txt"));
            // Scanner scanner = new Scanner(new File("day07\\test.txt"));
            rules = new ArrayList<>();
            while (scanner.hasNextLine()) {
                rules.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }

    public void run() {
        bags = new HashMap<>();
        for (String rule : rules) {
            parseRule(rule);
        }

        System.out.println(getBagsInShinygold("1shinygoldbag") - 1);

        // HashSet<String> colors = new HashSet<>();

        // for (String b : bags.keySet()) {
        //     colors.addAll(getColorsWithShinyGold(b));
        // }

        // System.out.println(colors.size());
    }

    // private HashSet<String> getColorsWithShinyGold(String b) {
    //     HashSet<String> colors = new HashSet<>();
    //     boolean containsGold = false;
    //     for (String bag : bags.get(b)) {
    //         if ("shinygoldbag".equals(bag))
    //             containsGold = true;
    //         colors.addAll(getColorsWithShinyGold(bag));
    //     }
    //     if (containsGold || colors.size() > 0) {
    //         colors.add(b);
    //     }
    //     return colors;
    // }

    private int getBagsInShinygold(String bag) {
        int count = 0;
        for (String s : bags.get(bag.substring(1))) {
            if (!"nootherbag".equals(s))
                count += getBagsInShinygold(s);
        }
        if (!"nootherbag".equals(bags.get(bag.substring(1)).get(0)))
            return count * Integer.parseInt(bag.substring(0, 1)) + Integer.parseInt(bag.substring(0, 1));
        return Integer.parseInt(bag.substring(0, 1));
    }

    private void parseRule(String rule) {
        rule = rule.replaceAll(" ", "");
        String[] parts = rule.split("contains{0,1}");
        String bag = parts[0].substring(0, parts[0].length() - 1);
        String[] insideBags = parts[1].split("s*,|s*\\.");

        ArrayList<String> bags = new ArrayList<>();
        for (int i = 0; i < insideBags.length; i++) {
            bags.add(insideBags[i]);
        }
        this.bags.put(bag, bags);
    }
}
