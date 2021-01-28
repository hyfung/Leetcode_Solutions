class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> vCandies(num_people, 0);

        int turn = 1;
        int counter = 0;
        while(candies > 0)
        {
            if (candies >= turn)
            {
                vCandies[counter] += turn;
                candies -= turn;
                counter++;
                turn++;
                counter %= num_people;
                
            } else
            {
                vCandies[counter] += candies;
                break;
            }
        }
        return vCandies;
    }
};
