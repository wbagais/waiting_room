<?php include("shared/header.php"); ?>

<!-- start banner Area -->
<section class="banner-area relative about-banner" id="home">
	<div class="overlay overlay-bg"></div>
	<div class="container">
		<div class="row d-flex align-items-center justify-content-center">
			<div class="about-content col-lg-12">
				<h1 class="text-white">
					CHECK IN
				</h1>
				<p class="text-white link-nav"><a href="index.php">Home </a>  <span class="lnr lnr-arrow-right"></span>  <a href="check_in.php"> Check In</a></p>
			</div>
		</div>
	</div>
</section>
<!-- End banner Area -->
<!-- Start appointment Area -->
<section class="team-area section-gap">
<section class="appointment-area">

	<div class="container">
		<div class="row justify-content-between align-items-center pb-120 appointment-wrap">

			<div class="col-lg-20 col-md-12 appointment-right pt-40 pb-40">
				<form name="check_in_form" class="form-wrap" action="http://students.hi.gmu.edu/cgi-bin/wbagais/check_in_db.cgi"  method="POST">
					<h3 class="pb-20 text-center mb-30">Check In</h3>
					<input type="text" class="form-control" name="id" placeholder="Patient ID" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Patient Name'" >
					<div class="form-select" id="service-select">
						
						<select name = "service">
									
							<option data-display="" disabled selected value>Service</option>
   							<option name = "service" value="1"> Check Up</option>
							<option name = "service" value="2"> Vaccination</option>
							<option name = "service" value="3"> Emergency</option>
						</select>
					</div>
					<div class="form-select" id="physician-select">
						<select name = "physician">
							<option data-display="" disabled selected value>Physician</option>
							<option name = "physician" value="1"> George Fisher</option>
							<option name = "physician" value="2"> Lena Caballero</option>
							<option name = "physician" value="3"> Thomas Slaughter</option>
							<option name = "physician" value="4"> Emily Beach</option>

						</select>
					</div>
					<button class="primary-btn text-uppercase">Confirm</button>
				</form>
			</div>
		</div>
	</div>
</section>
</section>

<!-- End appointment Area -->

<?php include("shared/footer.php"); ?>
