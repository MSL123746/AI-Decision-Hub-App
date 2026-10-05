import streamlit as st


st.set_page_config(
	page_title="AI Decision Hub",
	layout="wide",
	initial_sidebar_state="collapsed",
)

st.markdown(
	"""
	<style>
	:root {
		color-scheme: light;
	}

	.stApp {
		background: #ffffff;
		color: #20272b;
		font-family: "Segoe UI", Arial, sans-serif;
	}

	[data-testid="stHeader"] {
		background: transparent;
	}

	[data-testid="stAppDeployButton"] {
		display: none !important;
	}

	[data-testid="stMainMenu"] {
		display: none !important;
	}

	.block-container {
		max-width: 1440px;
		padding: 0.6rem 2.65rem 1.25rem;
	}

	h1 {
		color: #20272b;
		font-size: 1.9rem !important;
		font-weight: 700 !important;
		margin: 0 0 0.65rem !important;
	}

	.st-key-hub-title-row [data-testid="stHorizontalBlock"] {
		align-items: center;
	}

	.st-key-hub-title-icon {
		align-items: center;
		display: flex;
		justify-content: center;
		margin-bottom: 0.65rem;
	}

	.st-key-hub-title-icon img {
		display: block;
		object-fit: contain;
	}

	.st-key-hub-shell {
		background: #e7eeee;
		border: 0;
		border-radius: 9px;
		padding: 1.15rem 1.2rem 0.65rem;
	}

	.st-key-hub-shell [data-testid="stHorizontalBlock"] {
		gap: 0.8rem;
	}

	.st-key-hub-shell [data-testid="stHorizontalBlock"] > [data-testid="column"] + [data-testid="column"] {
		border-left: 1px solid #c2cccc;
		padding-left: 0.95rem;
	}

	.st-key-hub-shell label,
	.st-key-hub-shell [data-testid="stMarkdownContainer"] {
		color: #252c30;
		font-size: 0.94rem;
	}

	.field-heading,
	.audience-title {
		color: #20272b;
		font-size: 1.08rem;
		font-weight: 600;
		line-height: 1.25;
		margin: 0.45rem 0 0.55rem;
	}

	.audience-title {
		margin: 0 0 0.28rem;
	}

	.st-key-audience-box {
		background: rgba(255, 255, 255, 0.16);
		border: 1px solid #c5cece;
		border-radius: 8px;
		padding: 0.5rem 0.55rem 0.2rem;
	}

	.range-title {
		color: #252c30;
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.2rem;
	}

	.st-key-hub-shell [data-testid="stCheckbox"],
	.st-key-hub-shell [data-testid="stRadio"] {
		margin-bottom: 0.08rem;
	}

	.st-key-hub-shell [data-testid="stCheckbox"] label,
	.st-key-hub-shell [data-testid="stRadio"] label {
		font-size: 0.94rem;
	}

	.st-key-hub-shell [data-testid="stNumberInput"] input,
	.st-key-hub-shell [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
		background: #ffffff;
		border-color: #c1c9c9;
	}

	.st-key-hub-shell [data-testid="stButton"] button {
		background: #14232c;
		border: 0;
		border-radius: 8px;
		color: #ffffff;
		font-weight: 600;
		min-height: 2.55rem;
		width: 100%;
	}

	.st-key-hub-shell [data-testid="stButton"] button:hover {
		background: #263c48;
		border: 0;
		color: #ffffff;
	}

	.status-line {
		border-top: 1px solid #bdc8c8;
		margin-top: 0.85rem;
		padding-top: 0.7rem;
		text-align: center;
	}

	.status-line p {
		color: #697477;
		font-size: 0.9rem;
		margin: 0;
	}

	@media (max-width: 900px) {
		.block-container {
			padding: 1rem 1rem 1.25rem;
		}

		.st-key-hub-shell {
			padding: 0.9rem;
		}
	}
	</style>
	""",
	unsafe_allow_html=True,
)

with st.container(key="hub-title-row"):
	icon_column, title_column = st.columns([0.55, 8], vertical_alignment="center")
	with icon_column:
		with st.container(key="hub-title-icon"):
			st.image("home page icon.jpg", width=64)
	with title_column:
		st.title("AI Decision Hub")

with st.container(key="hub-shell"):
	title_columns = st.columns([2.25, 1.4, 1.0], gap="small")
	with title_columns[0]:
		model = st.selectbox(
			"Choose a Model",
			[
				"LR Campaign Optimization",
				"Customer Churn",
				"Consumer Purchase Behavior",
				"Customer Segmentation",
			],
			index=None,
			placeholder="Choose a Model",
			label_visibility="visible",
		)
	posting_column, platform_column, category_column, campaign_column, audience_column = st.columns(
		[1.05, 1.05, 1.05, 1.2, 1.08],
		gap="small",
	)

	with posting_column:
		st.markdown('<div class="field-heading">Posting Type</div>', unsafe_allow_html=True)
		st.checkbox("Video", value=True)
		st.checkbox("Image", value=True)
		st.checkbox("Announcement", value=True)
		st.checkbox("Podcast", value=False)
		st.markdown('<div class="field-heading">Promotion Type</div>', unsafe_allow_html=True)
		st.radio("Promotion Type", ["Organic", "Paid"], index=1, label_visibility="collapsed")

	with platform_column:
		st.markdown('<div class="field-heading">Platform</div>', unsafe_allow_html=True)
		st.checkbox("Instagram")
		st.checkbox("Facebook")
		st.checkbox("TikTok")
		st.checkbox("Snapchat")
		st.checkbox("Twitter (X)")

	with category_column:
		st.markdown('<div class="field-heading">Product Category</div>', unsafe_allow_html=True)
		st.checkbox("Apparel")
		st.checkbox("Shoes", value=True)
		st.checkbox("Cosmetics")
		st.checkbox("Home Goods")
		st.checkbox("Accessories")

	with campaign_column:
		st.markdown('<div class="field-heading">Campaign Details</div>', unsafe_allow_html=True)
		st.number_input("Posts Count", min_value=1, value=15, step=1)
		st.number_input("Event Duration (Days)", min_value=1, value=30, step=1)
		st.markdown('<div class="field-heading">Launch Details</div>', unsafe_allow_html=True)
		st.selectbox(
			"Launch Month",
			["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
			index=9,
		)
		st.number_input("Event Spend ($)", min_value=0.0, value=2500.0, step=100.0, format="%.2f")

	with audience_column:
		st.markdown('<div class="audience-title">Target Audience</div>', unsafe_allow_html=True)
		with st.container(key="audience-box"):
			st.markdown('<div class="range-title">Age Range</div>', unsafe_allow_html=True)
			st.number_input("Age Min", min_value=13, max_value=100, value=18, step=1)
			st.number_input("Age Max (Years)", min_value=13, max_value=100, value=35, step=1)
			st.markdown('<div class="field-heading">Gender</div>', unsafe_allow_html=True)
			st.checkbox("Female", value=True)
			st.checkbox("Male")

		predict_clicked = st.button("Predict", icon=":material/arrow_forward:")
		insights_clicked = st.button("AI Insights", icon=":material/auto_awesome:")

	st.markdown(
		'<div class="status-line"><p>Enter all data to view predictions.</p></div>',
		unsafe_allow_html=True,
	)

if predict_clicked:
	if model is None:
		st.warning("Choose a model before requesting a prediction.")
	else:
		st.info("The prediction service is not connected yet.")

if insights_clicked:
	st.info("AI insights are not connected yet.")
