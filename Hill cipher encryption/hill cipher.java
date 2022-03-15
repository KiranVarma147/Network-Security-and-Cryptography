import java.util.Scanner;

public class Hillcipher
{
    public static void main(String args[])
{
    Hillcipher hill=new Hillcipher();
    hill.input();
}

void input()
{
    Scanner sc=new Scanner(System.in);
    System.out.print("key: ");
    String key=sc.next();
    System.out.print("\nenter plain text: ");
    String pt=sc.next();
    encrypt(key,pt);
}

void encrypt(String key,String pt)
{
    int a=0;
    int mat[][]=new int[3][3];
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            mat[i][j]=(int)(key.charAt(a++))-65;
        }
    }
    int sum=0;
    System.out.print("encrypted data:");
    for(int i=0;i<3;i++)
    {
        sum=a=0;
        for(int j=0;j<3;j++)
        {
            sum+=mat[i][j]*((int)pt.charAt(a++)-65);
        }
    System.out.print((char)(65+sum%26));
    }
}
}