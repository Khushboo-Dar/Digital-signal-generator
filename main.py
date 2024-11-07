#Handles user input, manages the workflow, and coordinates different encoding/modulation techniques.
from ami import main_ami
from HDB3 import main_hdb3
from nrz_l import main_nrz_l
from diff_manchester import main_differential_manchester


def main():
    input_signal=input("Enter the signal you want to give as input:\n1.Digital Signal\n2. Analog Signal\n >>")
    if input_signal=="1":
        print("\nYou have chosen Digital Signal\n")
        line_encoding_technique=int(input("Enter the encoding technique you want to implement:\n1.NRZ_L\n2.Differential Manchester\n3.AMI\n >>"))
        
        
        if line_encoding_technique==1:
            main_nrz_l()

        elif line_encoding_technique==2:
            main_differential_manchester()

        elif line_encoding_technique==3:
            scramble = input("Do you want to use Scrambling for AMI? (y/n)").strip().lower()
            
            if scramble == "y":
                scramble_technique = input("Enter scrambling technique \n1.B8ZS\n2.HDB3)\n >> ")
                
                if scramble_technique == "2":
                    main_hdb3()

                elif scramble_technique == "1":
                    print("B8ZS is not available yet.")
                    return

                else:
                    print("Invalid scrambling technique selected for AMI.")
                    return


            elif scramble == "n":
                main_ami(bitrate, bits)

            else:
                print("Invalid input")
                return

        else:
            print("Invalid input")

    elif input_signal=="2":
        print("\nYou have chosen Analog Signal\n")
        print("This feature is not available yet")

if __name__ == "__main__":
    main()