#Handles user input, manages the workflow, and coordinates different encoding/modulation techniques.
from ami import main_ami
from HDB3 import main_hdb3
from nrz_l import main_nrz_l
from diff_manchester import main_differential_manchester
from dm import main_dm
from pcm import main_pcm
from nrz_i import main_nrz_i
from manchester import main_manchester
from scrambling_b8zs import main_b8zs

def main():
    input_signal=input("Enter the signal you want to give as input:\n1.Digital Signal\n2. Analog Signal\n >>")
    if input_signal=="1":
        print("\nYou have chosen Digital Signal\n")
        line_encoding_technique=int(input("Enter the encoding technique you want to implement:\n1.NRZ_L\n2.NRZ-I\n3.Manchester\n4.Differential Manchester\n5.AMI\n >>"))
        
        if line_encoding_technique==1:
            main_nrz_l()
        elif line_encoding_technique==2:
            main_nrz_i()
            
        elif line_encoding_technique==3:
            main_manchester()
            
        elif line_encoding_technique==4:
            main_differential_manchester()

        elif line_encoding_technique==5:
            scramble = input("Do you want to use Scrambling for AMI? (y/n)").strip().lower()
            
            if scramble == "y":
                scramble_technique = input("Enter scrambling technique \n1.B8ZS\n2.HDB3)\n >> ")
                
                if scramble_technique == "2":
                    main_hdb3()

                elif scramble_technique == "1":
                    main_b8zs()

                else:
                    print("Invalid scrambling technique selected for AMI.")
                    return


            elif scramble == "n":
                main_ami()

            else:
                print("Invalid input")
                return

        else:
            print("Invalid input")

    elif input_signal=="2":
        print("\nYou have chosen Analog Signal\n")
        modulation_technique=int(input("Enter the modulation technique you want to implement:\n1.PCM\n2.DM\n >>"))

        if modulation_technique==1:
            main_pcm()
            return
        elif modulation_technique==2:
            main_dm()

if __name__ == "__main__":
    main()